# from collections import deque
from sys import stdin

n = int(input())
l = []

for i in range(n):
    row = [int(j) for j in stdin.readline().split()]
    u = row[0]
    nodes = sorted(row[2:])
    l.append(dict(nodes = nodes, visited = False))

def dfs(i, time):
    if not l[i]['visited']:
        l[i]['visited'] = True
        l[i]['d'] = time
    time += 1
    for node in l[i]['nodes']:
        if l[node - 1]['visited']:
            continue
        time = dfs(node - 1, time)
        time += 1
    l[i]['f'] = time
    return time

time = 1
for i in range(n):
    if l[i]['visited']:
        continue    
    time = dfs(i, time)
    time += 1

for i, v in enumerate(l):
    print(i + 1, v['d'], v['f'])
