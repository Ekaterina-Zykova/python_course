"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from collections import defaultdict
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    long_words = []
    punctuation = """!"#$%&'()*+,./:;<=>?@[]^_`{|}~"""
    word_break = ""
    word_break2 = ""
    with open(file_path, "r", encoding="unicode-escape", errors="replace") as file:
        for line in file:
            # delete », «, —
            line = (
                line.lower()
                .strip()
                .strip("\u00bb")
                .strip("\u00ab")
                .replace("\u2014", "")
            )
            line = line.translate(str.maketrans("", "", punctuation))
            line = line.split()
            if line and line[-1][-1] == "-":
                if word_break:
                    word_break2 = line[-1][:-1]
                    word_break += line[0]
                    line = line[1:]
                else:
                    word_break = line[-1][:-1]
                line = line[:-1]
                line.append(word_break)
                word_break = word_break2
            for word in line:
                word = word.replace("-", "")
                if len(long_words) == 10:
                    if len(set(word)) > len(set(long_words[-1])):
                        long_words.append(word)
                        long_words.sort(key=len, reverse=True)
                        long_words.pop()
                else:
                    long_words.append(word)
                    long_words.sort(key=len, reverse=True)
    return long_words


def get_rarest_char(file_path: str) -> str:
    chars = defaultdict(int)
    with open(file_path, "r", encoding="unicode-escape", errors="replace") as file:
        for line in file:
            for word in line.split():
                for char in word.lower():
                    chars[char] += 1
    return min(chars, key=chars.get)


def count_punctuation_chars(file_path: str) -> int:
    counter = 0
    punctuation = """!"#$%&'()*+, -./:;<=>?@[]^_`{|}~"""
    with open(file_path, "r", encoding="unicode-escape", errors="replace") as file:
        for line in file:
            for word in line.split():
                for char in word:
                    if char in punctuation:
                        counter += 1
    return counter


def count_non_ascii_chars(file_path: str) -> int:
    ascii = tuple(range(128))
    counter = 0
    with open(file_path, "r", encoding="unicode-escape", errors="replace") as file:
        for line in file:
            for word in line:
                for char in word:
                    if ord(char) not in ascii:
                        counter += 1
    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    ascii = tuple(range(128))
    non_ascii_chars = defaultdict(int)
    with open(file_path, "r", encoding="unicode-escape", errors="replace") as file:
        for line in file:
            for word in line:
                for char in word:
                    if ord(char) not in ascii:
                        non_ascii_chars[char] += 1
    return max(non_ascii_chars, key=non_ascii_chars.get)
