import pytest

from homework5.save_original_info.save_original_info import custom_sum


@pytest.mark.parametrize(
    ["args", "expected_result"],
    [
        (([1, 2, 3], [4, 5]), [1, 2, 3, 4, 5]),
        ((1, 2, 3, 4), 10),
    ],
)
def test_custom_sum_with_print(args, expected_result, capsys):
    actual_result = custom_sum(*args)
    assert actual_result == expected_result
    assert capsys.readouterr().out.strip() == str(expected_result)


def test_custom_sum_without_print(capsys):
    without_print = custom_sum.__original_func
    result = without_print(1, 2, 3, 4)
    assert result == 10
    assert capsys.readouterr().out.strip() == ""


def test_func_save_original_info():
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"
    assert custom_sum.__name__ == "custom_sum"
