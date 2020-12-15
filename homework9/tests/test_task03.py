from pathlib import Path
from typing import Callable, Optional

import pytest

from homework9.task03.task03 import universal_file_counter


@pytest.mark.parametrize(
    ["text1", "text2", "tokenizer", "expected_result"],
    [
        ("1\n3\n5\n", "2\n4\n6\n", None, 6),
        ("1,3,5,", "2,4,6,", lambda string: string.split(","), 8),
        ("", "", str.split, 0),
    ],
)
def test_universal_file_counter(
    tmpdir, text1: str, text2: str, tokenizer: Optional[Callable], expected_result: int
):
    tmpdir.join("file1.txt").write(text1)
    tmpdir.join("file2.txt").write(text2)
    actual_result = universal_file_counter(Path(tmpdir), "txt", tokenizer)
    assert actual_result == expected_result
