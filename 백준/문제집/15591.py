import sys
from collections import deque

def BFS(k, v):
    count = 0 
    d = deque()
    d.append(v)
    visited = [0]*(N+1)
    visited[v] = 1
    r

    while d:
        x = d.popleft()
        for temp_v, temp_k in G[x]:
            if temp_k >= k and not visited[temp_v]:
                d.append(temp_v)
                count += 1
                visited[temp_v] = 1
    return count
            

N, Q = map(int, sys.stdin.readline().split())
G = [[] for _ in range(N+1)]

for i in range(N-1):
    p, q, r = map(int, sys.stdin.readline().split())
    G[p].append((q, r))
    G[q].append((p, r))

for i in range(Q):
    k, v = map(int, sys.stdin.readline().split())
    result = BFS(k, v)
    print(result)