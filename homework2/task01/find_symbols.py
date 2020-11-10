"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    long_words = []
    punctuation = """!"#$%&'()*+,-./:;<=>?@[]^_`{|}~"""
    paragraph = ""
    with open(file_path, "r", encoding="unicode-escape", errors="replace") as file:
        for line in file:
            if line != "\n":
                # delete \n, », «, —
                line = (
                    line.rstrip("\n")
                    .strip("\u00bb")
                    .strip("\u00ab")
                    .replace("\u2014", "")
                )
                if line[-1] == "-":
                    # join word break
                    paragraph += line
                else:
                    paragraph += line + " "
            else:
                paragraph = paragraph.lower().strip()
                paragraph = paragraph.translate(str.maketrans("", "", punctuation))
                for word in paragraph.split():
                    if len(long_words) < 10:
                        long_words.append(word)
                        long_words.sort(key=len, reverse=True)
                    else:
                        if len(word) > len(long_words[-1]):
                            long_words.append(word)
                            long_words.sort(key=len, reverse=True)
                            long_words.pop()
                        elif len(word) == len(long_words[-1]):
                            if len(set(word)) > len(set(long_words[0])):
                                long_words.pop()
                                long_words.append(word)
                paragraph = ""
    return long_words


def get_rarest_char(file_path: str) -> str:
    chars = dict()
    with open(file_path, "r", encoding="unicode-escape", errors="replace") as file:
        for line in file:
            for word in line.split():
                for char in word.lower():
                    chars[char] = chars.get(char, 0) + 1
    return min(chars, key=chars.get)


def count_punctuation_chars(file_path: str) -> int:
    counter = 0
    punctuation = """!"#$%&'()*+, -./:;<=>?@[]^_`{|}~"""
    list_char = []
    with open(file_path, "r", encoding="unicode-escape", errors="replace") as file:
        for line in file:
            for word in line.split():
                for char in word:
                    if char in punctuation:
                        counter += 1
    return counter


def count_non_ascii_chars(file_path: str) -> int:
    ascii = tuple(range(127))
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
    non_ascii_chars = dict()
    with open(file_path, "r", encoding="unicode-escape", errors="replace") as file:
        for line in file:
            for word in line:
                for char in word:
                    if ord(char) not in ascii:
                        non_ascii_chars[char] = non_ascii_chars.get(char, 0) + 1
    return max(non_ascii_chars, key=non_ascii_chars.get)
