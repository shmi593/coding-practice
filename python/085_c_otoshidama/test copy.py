N, Y = [int(n) for n in input().split()]

max_count_10000yen = Y / 10000
max_count_5000yen = Y / 5000
if max_count_10000yen > N:
    print("-1 -1 -1")
    exit()
elif max_count_10000yen == N:
    print(f"{N} 0 0")
    exit()
elif max_count_5000yen == N:
    print(f"0 {N} 0")
    exit()

max_count_1000yen = Y / 1000
if max_count_1000yen == N:
    print(f"0 0 {N}")
    exit()

"""
10x + 5y + z = (Y / 1000)
x + y + z = N

9x + 4y = (Y / 1000) - N
y = ( (Y / 1000) - N - 9x) / 4 
-> x でループして y が整数かどうかチェック
"""

for x in range(0, N + 1):
    y = (max_count_1000yen - N - (9 * x)) / 4
    if y.is_integer() and (x + y) <= N:
        y = int(y)
        print(f"{x} {y} {N - (x + y)}")
        exit()

print("-1 -1 -1")
