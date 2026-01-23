from sys import stdin

n = int(input())
A = [int(k) for k in stdin.readline().split()]
q = int(input())
mi = [int(k) for k in stdin.readline().split()]

sums = set()
for i in range(1 << n):
    patterns = []
    for j in range(n):
        if (i & 1 << j):
            patterns.append(A[j])

    sums.add(sum(patterns))

for m in mi:
    if m in sums:
        print("yes")
    else:
        print("no")
