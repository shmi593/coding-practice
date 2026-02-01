# https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c
from bisect import bisect_right
from sys import stdin


def solve(P, M) -> list[int]:
    ans = 0
    pair = sorted([m + n for m in P for n in P])
    for a in pair:
        if a > M:
            continue
        i = bisect_right(pair, M - a)
        ans = max(ans, (a + pair[i - 1]))
    return ans


N, M = tuple(map(int, stdin.readline().split()))
P = [int(stdin.readline()) for _ in range(N)] + [0]

print(solve(P, M))


# 独自で実装すると TLE
# def bisect_right(lst: list[int], n: int) -> int:
#     left = 0
#     mid = 0
#     right = len(lst) - 1
#     while left < right:
#         mid = (left + right) // 2
#         if n < lst[mid]:
#             right = mid
#         else:
#             left = mid + 1
#     return left
