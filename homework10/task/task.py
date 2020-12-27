import asyncio
import json
import re
import time
from operator import itemgetter
from typing import Optional

import aiohttp
from bs4 import BeautifulSoup

"""
Get information about companies from the site
https://markets.businessinsider.com/index/components/s&p_500 :
- Code and name;
- Current stock price in rubles;
- P/E;
- 1-year growth;
- Difference(profit) between 52 weeks highest and lowest stock price.

And create 4 json-files:
1) top-10 companies with the most expensive stocks in rubles;
2) top-10 companies with the lowest P/E;
3) top-10 companies that showed the highest growth in the last year;
4) top-10 companies that would bring the most profit.
"""


async def get_dollar_rate(page_content: str) -> float:
    soup = BeautifulSoup(page_content, "lxml").find("valute", id="R01235").value.string
    dollar_rate = float(soup.replace(",", "."))
    return dollar_rate


def get_p_e(soup) -> float:
    try:
        p_e = soup.find(
            "div", class_="snapshot__header", text="P/E Ratio"
        ).parent.text.split()[0]
        return float(p_e.replace(",", ""))
    except AttributeError:
        return 0


def get_potential_profit(soup) -> float:
    script = soup.find("div", id="snapshot").find("script")
    str_script = str(script.get_text)
    value = re.search(r"low52weeks: (\d*.\d*)", str_script)
    low = float(value.group().split()[1].replace(",", ""))
    value = re.search(r"high52weeks: (\d*.\d*)", str_script)
    high = float(value.group().split()[1].replace(",", ""))
    profit = round((high - low) / (low / 100), 2)
    return profit


async def get_page_company(
    session,
    company: dict,
    url: str,
    dollar_course: float,
) -> None:
    async with session.get(url) as response:
        soup = BeautifulSoup(await response.text(), "lxml")
        company["name"] = soup.find("span", class_="price-section__label").text.strip()
        company["code"] = soup.find(
            "span", class_="price-section__category"
        ).text.split()[-1]
        price = float(
            soup.find_all("span", class_="price-section__current-value")[
                -1
            ].text.replace(",", "")
        )
        company["price"] = round(price * dollar_course, 2)
        company["p_e"] = get_p_e(soup)
        company["profit"] = get_potential_profit(soup)


async def get_info_from_table(
    session,
    main_url: str,
    end_url: str,
    company_list: list,
    tasks: list,
    dollar_course: float,
    page: dict,
) -> Optional[str]:
    async with session.get(main_url + end_url, params=page) as response:
        soup = BeautifulSoup(await response.text(), "lxml")
        table = soup.find(class_="table table-small")
        if not table:
            return "end of table, all information is gotten"
        href_companies = [line.get("href") for line in table.find_all("a")]
        for href in href_companies:
            company = dict()
            company_list.append(company)
            company["growth"] = float(
                table.find(href=href).find_parent("tr").text.split()[-1][:-1]
            )
            url = main_url + href
            tasks.append(
                asyncio.create_task(
                    get_page_company(session, company, url, dollar_course)
                )
            )


async def create_4_json_files(company_list):
    price = [
        item
        for item in sorted(company_list, reverse=True, key=itemgetter("price"))[:10]
    ]
    p_e = [
        item for item in sorted(company_list, key=itemgetter("p_e")) if item["p_e"] > 0
    ][:10]
    growth = [
        item
        for item in sorted(company_list, reverse=True, key=itemgetter("growth"))[:10]
    ]
    profit = [
        item
        for item in sorted(company_list, reverse=True, key=itemgetter("profit"))[:10]
    ]
    top_10 = [price, p_e, growth, profit]
    names_for_files = ["price", "p_e", "growth", "profit"]
    for i in range(len(top_10)):
        with open(f"top_10_{names_for_files[i]}.json", "w") as file:
            result_dict = [
                {
                    "name": item["name"],
                    "code": item["code"],
                    f"{names_for_files[i]}": item[f"{names_for_files[i]}"],
                }
                for item in top_10[i]
            ]
            file.write(json.dumps(result_dict, indent=4))


async def get_info(main_url: str, end_url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get("http://www.cbr.ru/scripts/XML_daily.asp") as resp:
            dollar_course = await get_dollar_rate(await resp.text())
        tasks = []
        page = {"p": 1}
        company_list = []
        while True:
            result = await get_info_from_table(
                session,
                main_url,
                end_url,
                company_list,
                tasks,
                dollar_course,
                page,
            )
            if result == "end of table, all information is gotten":
                break
            page["p"] += 1

        await asyncio.gather(*tasks)
        await create_4_json_files(company_list)


if __name__ == "__main__":
    main_site = "https://markets.businessinsider.com"
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(
        get_info(main_site, "/index/components/s&p_500")
    )
    print(time.time() - start_time)
