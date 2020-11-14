import os

import pytest

from homework4.task01.read_file import read_magic_number


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("1", True),
        ("3", False),
    ],
)
def test_read_magic_number(tmpdir, value: str, expected_result: bool):
    tmp_dir = tmpdir.mkdir("subdir")
    tmp_file = tmp_dir.join("test.txt")
    tmp_file.write(value)
    tmp_path = os.path.join(tmp_file.dirname, tmp_file.basename)
    actual_result = read_magic_number(tmp_path)
    tmp_file.remove()
    assert actual_result == expected_result


def test_read_magic_number_with_exception(tmpdir):
    tmp_dir = tmpdir.mkdir("subdir")
    tmp_file = tmp_dir.join("test.txt")
    tmp_file.write("value")
    tmp_path = os.path.join(tmp_file.dirname, tmp_file.basename)
    with pytest.raises(ValueError, match="Digit required"):
        read_magic_number(tmp_path)
    tmp_file.remove()
