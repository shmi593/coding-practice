# https://atcoder.jp/contests/abs/tasks/practice_1
from sys import stdin


def solve(a, b, c, s):
    return f"{a + b + c} {s}"


a = int(input())
b, c = tuple(map(int, stdin.readline().split()))
s = input()

print(solve(a, b, c, s))
