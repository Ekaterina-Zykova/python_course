from pathlib import Path

import aiohttp
from aioresponses import aioresponses
from bs4 import BeautifulSoup

from homework10.task.task import (
    create_4_json_files,
    get_dollar_rate,
    get_info_from_table,
    get_p_e,
    get_page_company,
    get_potential_profit,
)

correct_company_list = [
    {
        "name": "YUM! Brands Inc.",
        "code": "YUM",
        "p_e": 28.75,
        "price": 7924.85,
        "growth": -2.78,
        "profit": 100.45,
    },
    {
        "name": "Zimmer Biomet",
        "code": "ZBH",
        "p_e": 19.10,
        "price": 11071.78,
        "growth": -10.37,
        "profit": 117.94,
    },
    {
        "name": "Zions Bancorporation",
        "code": " ZION",
        "p_e": 12.38,
        "price": 3215.08,
        "growth": -25.32,
        "profit": 122.52,
    },
    {
        "name": "Zoeti a",
        "code": "ZTS",
        "p_e": 36.49,
        "price": 11922.66,
        "growth": 11.49,
        "profit": 95.68,
    },
]


def test_get_p_e():
    with open("page_company.html") as file:
        soup = BeautifulSoup(file.read(), "lxml")
        assert get_p_e(soup) == 28.75


def test_get_potential_profit():
    with open("page_company.html") as file:
        soup = BeautifulSoup(file.read(), "lxml")
        assert get_potential_profit(soup) == 100.45


async def test_create_4_json_files():
    await create_4_json_files(correct_company_list)
    assert len(sorted(Path(".").glob("*.json"))) == 4


async def test_get_dollar_rate():
    with open("xml_daily.xml") as file:
        assert await get_dollar_rate(file.read()) == 73.6921


async def test_get_info_from_table():
    main_site = "https://markets.businessinsider.com"
    end_url = "/index/components/s&p_500"
    tasks = []
    page = {"p": 11}
    company_list = []
    dollar_course = 73.6921
    with open("page_table.html") as file:
        with aioresponses() as mocked:
            url = "https://markets.businessinsider.com/index/components/s&p_500?p=11"
            mocked.get(url, body=file.read())
            session = aiohttp.ClientSession()
            await get_info_from_table(
                session,
                main_site,
                end_url,
                company_list,
                tasks,
                dollar_course,
                page,
            )
            assert company_list == [
                {"growth": -2.78},
                {"growth": -10.37},
                {"growth": -25.32},
                {"growth": 11.49},
            ]


async def test_get_page_company():
    company = {"growth": -2.78}
    dollar_course = 73.6921
    with open("page_company.html") as file:
        with aioresponses() as mocked:
            url = "https://markets.businessinsider.com/stocks/yum-stock"
            mocked.get(url, body=file.read())
            session = aiohttp.ClientSession()
            await get_page_company(
                session,
                company,
                url,
                dollar_course,
            )
            assert company == {
                "code": "YUM",
                "growth": -2.78,
                "name": "YUM! Brands Inc.",
                "p_e": 28.75,
                "price": 7924.85,
                "profit": 100.45,
            }
