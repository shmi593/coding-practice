import math

P = float(input())
# x > 0, p > 0
f = lambda x: x + P / (2 ** (2 / 3 * x))
fd = lambda x: 1 + P * (2 ** -(2 / 3 * x)) * math.log(2** -(2 / 3))

l = 0
r = P

for _ in range(10000):
    mid = (l + r) / 2
    fdx = fd(mid)
    if fdx == 0:
        break
    elif fdx > 0:
        r = mid
    elif fdx < 0:
        l = mid

print(f(mid))
