import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
visited = [False]*(N+1)

G = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    G[a].append(b)
    G[b].append(a)

for i in range(N+1):
    G[i].sort()

def DFS(node):
    print(node, end=' ')
    visited[node]=True
    for i in G[node]:
        if not visited[i]:
            DFS(i)

def BFS(node):
    q = deque([node])
    visited[node] = True
    while q:
        a = q.popleft()
        print(a, end=' ')
        for i in G[a]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

DFS(V)
visited = [False]*(N+1)
print()
BFS(V)
            
        
