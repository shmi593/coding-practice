import math

owned_number_500yen = int(input())
owned_number_100yen = int(input())
owned_number_50yen = int(input())
total = int(input())

if not total % 50 == 0:
    print(0)
    exit()

if not (total % 100 == 0) and owned_number_50yen == 0:
    print(0)
    exit()

possible_number_patterns = {
    '500yen': min(owned_number_500yen, math.floor(total / 500)), 
    '100yen': min(owned_number_100yen, math.floor(total / 100))
}
max_total_50yen = owned_number_50yen * 50 

pattern = 0
for total_500yen in range(0, (possible_number_patterns['500yen'] + 1) * 500, 500):
    for total_100yen in range(0 , (possible_number_patterns['100yen'] + 1) * 100, 100):
        total_50yen = total - (total_500yen + total_100yen)
        if total_50yen < 0:
            break
        if max_total_50yen >= total_50yen:
            pattern += 1

print(pattern)