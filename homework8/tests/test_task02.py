import sqlite3
from typing import Any, Tuple

import pytest

from homework8.task02.task02 import TableData

presidents = TableData(database_name="example.sqlite", table_name="presidents")


@pytest.mark.parametrize(
    ["table", "key", "expected_result"],
    [
        (presidents, "Yeltsin", ("Yeltsin", 999, "Russia")),
        (presidents, "Russia", ("Yeltsin", 999, "Russia")),
        (presidents, "Trump", ("Trump", 1337, "US")),
        (presidents, "Big Man Tyrone", ("Big Man Tyrone", 101, "Kekistan")),
        (presidents, "101", ("Big Man Tyrone", 101, "Kekistan")),
    ],
)
def test_getitem(table: TableData, key: str, expected_result: Tuple[Any]):
    actual_result = table[key]
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["table", "item", "expected_result"],
    [
        (presidents, "Yeltsin", True),
        (presidents, "Ivanov", False),
    ],
)
def test_contains(table: TableData, item: str, expected_result: bool):
    actual_result = item in table
    assert actual_result is expected_result


def test_iter():
    actual_result = [president["name"] for president in presidents]
    assert actual_result == ["Yeltsin", "Trump", "Big Man Tyrone"]


def test_len():
    assert len(presidents) == 3
    conn = sqlite3.connect("example.sqlite")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO presidents VALUES ('Ivanov', 100, 'Country')")
    conn.commit()
    conn.close()
    assert len(presidents) == 4
