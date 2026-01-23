a, b, c, x, y = [int(s) for s in input().split()]

if (a + b) <= (2 * c):
    print((a * x) + (b * y))
    exit()

if (2 * c) <= min(a, b):
    print(2 * c * max(x, y))
    exit() 

more_preparing_pizza = {'amount': a, 'qty': x} if x > y else {'amount': b, 'qty': y}

amount_list = []
# 2c < a + b
# 2c - a < b かつ 2c - b < a   
# つまり、準備する数が少ないピザを ABピザ2枚に置き換えてもよい
for n in range(min(x, y), more_preparing_pizza['qty'] + 1):
    amount_list += [more_preparing_pizza['amount'] * (more_preparing_pizza['qty'] - n) + 2 * c * n]

print(min(amount_list))
