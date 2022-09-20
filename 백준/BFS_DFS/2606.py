import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

G = [[] for _ in range(N+1)]

check = 0
visited = [False]*(N+1)
q = deque()

for i in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    G[x].append(y)
    G[y].append(x)

q.append(1)
visited[1] = True

while q:
    temp = q.popleft()
    for i in G[temp]:
        if not visited[i]:
            q.append(i)
            visited[i] = True
            check += 1

print(check)
            