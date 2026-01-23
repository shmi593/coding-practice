from sys import stdin

n = int(input())
# { } is set
print(len( {int(stdin.readline()) for _ in range(n)} ))
