from itertools import product
 
N = int(input())
S = input()
ans = 0
 
# 重複のない"0123456789"からなる3文字
for P in product("0123456789", repeat=3):
    i = -1
    # 重複なしの3文字をループ
    print(P)
    for p in P:
        # 見つからなかったら-1を返す
        # S[i+1]からpを探し、インデックスをiにする
        i = S.find(p, i + 1)
        if i == -1:
            break
    if i != -1:
        print(i)
        ans += 1
 
print(ans)