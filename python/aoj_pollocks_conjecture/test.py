# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1167&lang=jp
from sys import stdin, maxsize


pollock_conjecture = lambda n: n * (n + 1) * (n + 2) // 6

max = 10**6
dp = [maxsize] * (max + 1)
odddp = [maxsize] * (max + 1)
dp[0] = odddp[0] = 0

# pollock_conjecture(180) = 988260
# pollock_conjecture(181) = 1004731 > 10**6
for i in range(1, 181):
    num = pollock_conjecture(i)
    for j in range(num, max + 1):
        new_value = dp[j - num] + 1
        if new_value < dp[j]:
            dp[j] = new_value
        if num % 2 == 1:
            new_value_odd = odddp[j - num] + 1
            if new_value_odd < odddp[j]:
                odddp[j] = new_value_odd

while True:
    n = int(stdin.readline())
    if n == 0:
        break
    print(dp[n], odddp[n])
