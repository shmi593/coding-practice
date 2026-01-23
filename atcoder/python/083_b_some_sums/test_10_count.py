n, a, b = [int(s) for s in input().split()]

total = sum([i for i in range(a, min(n, b, 9) + 1)])
if n < 10:
    print(total)
    exit()

for num in range(10, n + 1, 10):
    s = str(num)
    total_except_ones_place = sum(map(int, s))
    if b < total_except_ones_place:
        continue
    sum_for_added_ones_place = sum([num + i for i in range(max(0, a - total_except_ones_place), min(b - total_except_ones_place + 1, (n - num + 1), 10))])
    total += sum_for_added_ones_place 

print(total)
