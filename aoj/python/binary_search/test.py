# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B
from sys import stdin


def solve(n: int, S: list[int], T: list[int]) -> int:
    ans = 0
    for t in T:
        if find_number(S, t, 0, n - 1) >= 0:
            ans += 1
    return ans


def find_number(S: list[int], t: int, start: int, end: int) -> int:
    mid = (start + end) // 2
    if t == S[mid]:
        return mid
    elif end - start < 1:
        return -1
    elif t < S[mid]:
        return find_number(S, t, start, mid - 1)
    elif t > S[mid]:
        return find_number(S, t, mid + 1, end)


n = int(input())
S = list(map(int, stdin.readline().split()))
_q = int(input())
T = list(map(int, stdin.readline().split()))

print(solve(n, S, T))
