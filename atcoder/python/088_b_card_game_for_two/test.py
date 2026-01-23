_n = int(input())
a = [int(s) for s in input().split()]

desc_cards = sorted(a, reverse=True) 

print(sum(desc_cards[0::2]) - sum(desc_cards[1::2]))
