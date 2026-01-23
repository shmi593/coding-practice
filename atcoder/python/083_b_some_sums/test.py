n, a, b = [int(s) for s in input().split()]

total = sum([i for i in range(a, min(n, b, 9) + 1)])
if n < 10:
    print(total)
    exit()

for digit in range(1, len(str(n))):
    for num in range(10 ** digit, min((n + 1), 10 ** (digit + 1))):
        s = str(num)
        if int(s[0]) > b:
            break
        each_digit_total = sum(map(int, s))
        if a <= each_digit_total and each_digit_total <= b:
            total += num

print(total)
