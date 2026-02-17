# https://atcoder.jp/contests/joi2009ho/tasks/joi2009ho_b
from bisect import bisect_right
from sys import stdin


def solve(stores, destinations):
    total = 0
    for dest in destinations:
        i = bisect_right(stores, dest)
        total += min(abs(dest - stores[i - 1]), abs(dest - stores[i]))
    return total


d = int(stdin.readline())
n = int(stdin.readline())
m = int(stdin.readline())
stores = sorted([0] + [int(stdin.readline()) for _ in range(n - 1)] + [d])
destinations = [int(stdin.readline()) for _ in range(m)]

print(solve(stores, destinations))
