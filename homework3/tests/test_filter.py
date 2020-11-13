from typing import Any, Callable, Dict, List, Sequence

import pytest

from homework3.task03.filter import Filter, make_filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ({"name": "polly", "type": "bird"}, [sample_data[1]]),
        ({"type": "person", "name": "Bill"}, [sample_data[0]]),
        ({"name": "polly", "occupation": "was here"}, []),
        ({}, []),
    ],
)
def test_make_filter(value: Dict[Any, Any], expected_result: List[Any]):
    actual_result = make_filter(**value).apply(sample_data)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["func", "expected_result"],
    [
        (
            (lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)),
            [2, 4, 6, 8, 10, 12, 14, 16, 18],
        )
    ],
)
def test_filter(func: Sequence[Callable], expected_result: List[Any]):
    actual_result = Filter(*func).apply(range(20))
    assert actual_result == expected_result
