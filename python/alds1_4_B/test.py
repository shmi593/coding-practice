from sys import stdin

n = int(input())
S = [int(k) for k in stdin.readline().split()]
q = int(input())
T = [int(k) for k in stdin.readline().split()]

ans = 0
for num in T:
    l = 0
    r = len(S) - 1
    m = r // 2
    while l <= r:
        # end binary search
        if num == S[m]:
            ans += 1
            break
        # continue binary search
        if num > S[m]:
            l = m + 1
        else:
            r = m - 1
        m = (l + r) // 2

print(ans)
