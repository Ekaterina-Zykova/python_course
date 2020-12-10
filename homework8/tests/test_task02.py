import sqlite3
from typing import Any, Tuple

import pytest

from homework8.task02.task02 import TableData


@pytest.mark.parametrize(
    ["key", "expected_result"],
    [
        ("Yeltsin", ("Yeltsin", 999, "Russia")),
        ("Russia", ("Yeltsin", 999, "Russia")),
        ("Trump", ("Trump", 1337, "US")),
        ("Big Man Tyrone", ("Big Man Tyrone", 101, "Kekistan")),
        ("101", ("Big Man Tyrone", 101, "Kekistan")),
    ],
)
def test_getitem(key: str, expected_result: Tuple[Any]):
    with TableData(
        database_name="example.sqlite", table_name="presidents"
    ) as presidents:
        assert presidents[key] == expected_result


@pytest.mark.parametrize(
    ["item", "expected_result"],
    [
        ("Yeltsin", True),
        ("Ivanov", False),
    ],
)
def test_contains(item: str, expected_result: bool):
    with TableData(
        database_name="example.sqlite", table_name="presidents"
    ) as presidents:
        actual_result = item in presidents
        assert actual_result is expected_result


def test_iter():
    with TableData(
        database_name="example.sqlite", table_name="presidents"
    ) as presidents:
        actual_result = [president["name"] for president in presidents]
        assert actual_result == ["Yeltsin", "Trump", "Big Man Tyrone"]


def test_len():
    with TableData(
        database_name="example.sqlite", table_name="presidents"
    ) as presidents:
        assert len(presidents) == 3
        conn = sqlite3.connect("example.sqlite")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO presidents VALUES ('Ivanov', 100, 'Country')")
        conn.commit()
        conn.close()
        assert len(presidents) == 4
