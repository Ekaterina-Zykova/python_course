import os

import pytest

from homework8.task01.task01 import KeyValueStorage


def test_key_value_storage(tmpdir):
    tmp_dir = tmpdir.mkdir("subdir")
    tmp_file = tmp_dir.join("test.txt")
    tmp_file.write(
        """name=kek
                    last_name=top
                    power=9001
                    song=shadilay"""
    )
    tmp_path = os.path.join(tmp_file.dirname, tmp_file.basename)
    storage = KeyValueStorage(tmp_path)
    tmp_file.remove()
    assert storage["name"] == storage.name == "kek"
    assert storage["last_name"] == storage.last_name == "top"
    assert storage["power"] == storage.power == 9001
    assert storage["song"] == storage.song == "shadilay"


def test_key_value_storage_with_error(tmpdir):
    tmp_dir = tmpdir.mkdir("subdir")
    tmp_file = tmp_dir.join("test.txt")
    tmp_file.write("""1=something""")
    tmp_path = os.path.join(tmp_file.dirname, tmp_file.basename)
    with pytest.raises(ValueError) as exc:
        KeyValueStorage(tmp_path)
        tmp_file.remove()
    assert str(exc.value) == "Key starts with a digit, key cannot be an attribute"
