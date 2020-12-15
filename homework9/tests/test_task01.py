import pytest

from homework9.task01.task01 import merge_sorted_files


@pytest.mark.parametrize(
    ["text1", "text2", "text3"],
    [
        ("1\n3\n5\n", "2\n4\n6\n", ""),
        ("1\n2\n", "3\n4\n", "5\n6\n"),
        ("1\n2\n5\n6\n", "3\n4\n", ""),
    ],
)
def test_merge_sorted_files(tmpdir, text1: str, text2: str, text3: str):
    tmpdir.join("file1.txt").write(text1)
    tmpdir.join("file2.txt").write(text2)
    tmpdir.join("file3.txt").write(text3)
    actual_result = list(merge_sorted_files(tmpdir.listdir()))
    assert actual_result == [1, 2, 3, 4, 5, 6]
