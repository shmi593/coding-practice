N = int(input())
S = input()
chars = list(S)

ans = 0
set_d_1 = set()
for i in range(0, N - 2):
    if chars[i] in set_d_1:
        continue
    set_d_2 = set()
    for j in range(i + 1, N - 1):
        if chars[j] in set_d_2:
            continue
        set_d_2.add(chars[j]) 
        set_d_3 = set(chars[j + 1:])
        ans += len(set_d_3)
    set_d_1.add(chars[i])

print(ans)
