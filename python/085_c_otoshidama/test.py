N, Y = [int(n) for n in input().split()]

def print_then_exit(s): 
    print(s)
    exit()
 
max_count_10000yen = Y / 10000
max_count_10000yen > N and print_then_exit("-1 -1 -1")
max_count_10000yen == N and print_then_exit(f"{N} 0 0")

max_count_1000yen = Y / 1000
max_count_1000yen < N and print_then_exit("-1 -1 -1")
max_count_1000yen == N and print_then_exit(f"0 0 {N}")

"""
10x + 5y + z = (Y / 1000)
x + y + z = N

9x + 4y = (Y / 1000) - N
y = ( (Y / 1000) - N - 9x ) / 4 
-> x でループして y が整数かどうかチェック
"""
for x in range(0, N + 1):
    y = (max_count_1000yen - N - (9 * x)) / 4
    if y < 0:
        break
    if y.is_integer() and (x + y) <= N:
        y = int(y)
        print_then_exit(f"{x} {y} {N - (x + y)}")

print("-1 -1 -1")
