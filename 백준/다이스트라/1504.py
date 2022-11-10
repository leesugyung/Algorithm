import sys
import heapq

INF = sys.maxsize
N, E = map(int, sys.stdin.readline().split())

G = [[] for _ in range(N+1)]

for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    G[a].append((b, c))
    G[b].append((a, c))

v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(start, end):
    h = []
    heapq.heappush(h, (0, start))
    visited = [0]*(N+1)
    road = [INF]*(N+1)
    road[start] = 0

    while h:
        w, v = heapq.heappop(h)
        if v == end:
            return road[end]
        for temp_v, temp_w in G[v]:
            if not visited[temp_v]:
                if road[temp_v] > w+temp_w:
                    road[temp_v] = w+temp_w
                    heapq.heappush(h, (road[temp_v],temp_v))
        visited[v] = 1
    return road[end]

x = dijkstra(v1, v2)
case1 = dijkstra(1, v1)+ dijkstra(v2, N)+ x

case2 = dijkstra(1, v2)+ dijkstra(v1, N)+ x

sum = min(case1, case2)

if sum >= INF:
    print(-1)
else:
    print(sum)