from sys import stdin

N, W = map(int, stdin.readline().split())

values = []
weights = []
for i in range(N):
    v, w = map(int, stdin.readline().split())
    values.append(v)
    weights.append(w)

dp = [[0] * (W + 1) for _ in range(N + 1)]
for i in range(N + 1):
    if i == 0:
        continue
    for w in range(W + 1):
        if w >= weights[i - 1]:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
        else:
            dp[i][w] = dp[i - 1][w]

print(dp[N][W])
