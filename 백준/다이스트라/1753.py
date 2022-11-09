'''
<실수한 부분>
1. 메모리 초과
처음에 행렬을 만들어서 G를 만들었다. 하지만 이렇게 되면 경로가 없는 vertex간의 관계까지 표현하므로 메모리 낭비가 많이 된다.

2. 큐에서 가장 먼저 꺼내야 하는 것은 
그 정점까지의 최단 거리가 가장 짧은 것이지, 가중치가 가장 작은 간선의 목적지가 아니다!!

<처음 안 부분>
for w, next_node in graph[now]: -> 오잉 이렇게도 되는구나;; 안되는게 없는듯
G = [[] for _ in range(V+1)] -> 이것도 뭔가 신기함

'''

import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

G = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    G[u].append([v,w])

route = [11*V]*(V+1)
route[K] = 0

h = []
heapq.heappush(h, (0, K))
visited = [0]*(V+1)

while h:
    temp = heapq.heappop(h)[1]
    for i in range(len(G[temp])):
        r, c = G[temp][i][0], G[temp][i][1]
        if not visited[r]:
            if c+route[temp]<route[r]:
                route[r] = c+route[temp]
                heapq.heappush(h, (route[r], r))
    visited[temp] = 1

for i in range(1, V+1):
    if route[i]==11*V:
        print("INF")
    else:
        print(route[i])