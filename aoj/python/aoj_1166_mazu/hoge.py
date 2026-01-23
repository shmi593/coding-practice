import numpy as np

a = np.array(range(10))
print("a = ", a)
b = a + 100
print("b = ", b)

# インデックス使っちゃうとこんな感じ
result1 = []
for i in range(10):
    answer = a[i] * 2 if b[i] % 2 == 0 else a[i] * 3
    result1.append(answer)
print(np.array(result1))

# np.whereと関数を使えば１行で書けて速い


def func_double(x):
    return x * 2


def func_triple(x):
    return x * 3


result2 = np.where(b % 2 == 0, func_double(a), func_triple(a))
print(result2)
