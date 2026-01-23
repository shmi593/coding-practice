from sys import stdin

def is_in_time(score, H, S):
    max_limits = []
    for i in range(N):
        # score に対して各風船を割るのにかけていい最大時間(秒)
        max_limits.append((score - H[i]) // S[i])
    max_limits.sort()
    return all([n <= max_limits[n] for n in range(N)])

def binary_search(H, S):
    # (min, max]
    min = 0
    max = int(1e+14)
    while (abs(max - min) > 1):
        mid = (max + min) // 2
        if is_in_time(mid, H, S):
            max = mid
        else:
            min = mid
    return max

N = int(input())
H = []
S = []
for i in range(N):
    h, s = map(int, stdin.readline().split())
    H.append(h)
    S.append(s)

print(binary_search(H, S))
