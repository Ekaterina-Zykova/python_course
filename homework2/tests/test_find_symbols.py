import os
from typing import List

import pytest

import homework2.task01.find_symbols


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (
            os.path.join("homework2", "data.txt"),
            [
                "verfassungsverletzungen",
                "mehrheitsvorstellungen",
                "politischstrategischen",
                "souveränitätsansprüche",
                "symbolischsakramentale",
                "wiederbelebungsübungen",
                "werkstättenlandschaft",
                "geschichtsphilosophie",
                "menschheitsgeschichte",
                "werkstättenlandschaft",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(file_path: str, expected_result: List[str]):
    actual_result = homework2.task01.find_symbols.get_longest_diverse_words(file_path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (os.path.join("homework2", "data.txt"), "›"),
    ],
)
def test_get_rarest_char(file_path: str, expected_result: str):
    actual_result = homework2.task01.find_symbols.get_rarest_char(file_path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (os.path.join("homework2", "data.txt"), 5305),
    ],
)
def test_count_punctuation_chars(file_path: str, expected_result: int):
    actual_result = homework2.task01.find_symbols.count_punctuation_chars(file_path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (os.path.join("homework2", "data.txt"), 2972),
    ],
)
def test_count_non_ascii_chars(file_path: str, expected_result: int):
    actual_result = homework2.task01.find_symbols.count_non_ascii_chars(file_path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (os.path.join("homework2", "data.txt"), "ä"),
    ],
)
def test_get_most_common_non_ascii_char(file_path: str, expected_result: str):
    actual_result = homework2.task01.find_symbols.get_most_common_non_ascii_char(
        file_path
    )
    assert actual_result == expected_result
