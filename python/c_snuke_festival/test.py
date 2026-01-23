import bisect

from sys import stdin

N = int(input())
A = sorted([int(k) for k in stdin.readline().split()])
B = sorted([int(k) for k in stdin.readline().split()])
C = sorted([int(k) for k in stdin.readline().split()])

ans = 0
for b in B:
    p_a = bisect.bisect_left(A, b)
    p_c = N - bisect.bisect_right(C, b)
    ans += p_a * p_c

print(ans)
