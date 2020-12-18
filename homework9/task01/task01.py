"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
import heapq
from pathlib import Path
from typing import Iterator, List, Union


def read_as_ints(file_name):
    with open(file_name) as file:
        for line in file:
            yield int(line)


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    files = (read_as_ints(name) for name in file_list)
    for line in heapq.merge(*files):
        yield line
