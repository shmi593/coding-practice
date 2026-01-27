# https://atcoder.jp/contests/abc106/tasks/abc106_b

N = int(input())
ans = 0


def solve(N):
    ans = 0
    for n in range(1, N + 1, 2):
        count = 0
        for m in range(1, n + 1):
            if n % m == 0:
                count += 1
        if count == 8:
            ans += 1
    return ans


print(solve(N))
