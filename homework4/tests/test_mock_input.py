from unittest import mock

import pytest

from homework4.task02.mock_input import count_dots_on_i


def mock_urlopen(*args, **kwargs):
    return "iiiii"


def test_count_dots_on_i_():
    with mock.patch("urllib.request.urlopen", new=mock_urlopen):
        result = count_dots_on_i("https://example.com/")
        assert result == 5


def test_count_dots_on_i_with_error():
    with mock.patch("urllib.request.urlopen") as mock_urlopen:
        mock_urlopen.side_effect = ValueError
        with pytest.raises(ValueError):
            count_dots_on_i("https://example.com/")
