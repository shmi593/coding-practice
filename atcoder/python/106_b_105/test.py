n = int(input())

l = [i for i in range(105, n + 1, 2)]

def has_exactly_six(odd, divisors, count = 0):
    for divisor in divisors:
        quotient = odd / divisor
        if quotient.is_integer():
            count += 2
            next_divisors = list(range(divisor + 2, int(quotient) - 1, 2))
            return has_exactly_six(odd, next_divisors, count)
    return count == 6

def solve(l):
    matches = [odd for odd in l if has_exactly_six(odd, list(range(3, odd - 1, 2)))]
    return len(matches)

print(solve(l))
