import os
from typing import List

import pytest

from homework2.task01.find_symbols import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)

file_path = os.path.join("homework2", "data.txt")


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (
            file_path,
            [
                "werkstättenlandschaft",
                "zoologischpolitischen",
                "werkstättenlandschaft",
                "entscheidungsschlacht",
                "résistancebewegungen",
                "bevölkerungsabschub",
                "kollektivschuldiger",
                "unmißverständliche",
                "friedensabstimmung",
                "selbstverständlich",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(file_path: str, expected_result: List[str]):
    actual_result = get_longest_diverse_words(file_path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (file_path, "›"),
    ],
)
def test_get_rarest_char(file_path: str, expected_result: str):
    actual_result = get_rarest_char(file_path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (file_path, 5305),
    ],
)
def test_count_punctuation_chars(file_path: str, expected_result: int):
    actual_result = count_punctuation_chars(file_path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (file_path, 2972),
    ],
)
def test_count_non_ascii_chars(file_path: str, expected_result: int):
    actual_result = count_non_ascii_chars(file_path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (file_path, "ä"),
    ],
)
def test_get_most_common_non_ascii_char(file_path: str, expected_result: str):
    actual_result = get_most_common_non_ascii_char(file_path)
    assert actual_result == expected_result
