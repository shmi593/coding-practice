# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2199&lang=jp
from sys import stdin, maxsize


def solve(C, X):
    dp = [[maxsize] * 256 for _ in range(len(X))]
    dp[0][128] = 0
    for i in range(1, len(X)):
        for j in range(256):
            if dp[i - 1][j] == maxsize:
                continue
            for Ck in C:
                yn = roundfrom0to255(j + Ck)
                dp[i][yn] = (
                    dp[i - 1][j] + (yn - X[i]) ** 2
                    if dp[i][yn] == maxsize
                    else min(dp[i][yn], dp[i - 1][j] + (yn - X[i]) ** 2)
                )
    return min(dp[-1])


roundfrom0to255 = lambda x: 0 if x < 0 else 255 if x > 255 else x


while True:
    N, M = map(int, stdin.readline().split())
    if N == 0 and M == 0:
        break
    C = {int(stdin.readline()) for _ in range(M)}
    X = [128] + [int(stdin.readline()) for _ in range(N)]
    print(solve(C, X))
