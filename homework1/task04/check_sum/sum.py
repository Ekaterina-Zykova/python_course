"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    count = 0
    ab_sum = dict()
    for i in a:
        for j in b:
            if i + j not in ab_sum:
                ab_sum[i + j] = 1
            else:
                ab_sum[i + j] += 1
    for k in c:
        for l in d:
            if -(k + l) in ab_sum:
                count += ab_sum[-(k + l)]
    return count
