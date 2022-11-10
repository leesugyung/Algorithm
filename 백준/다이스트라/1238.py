import sys
import heapq

INF = sys.maxsize
N, M, X = map(int, sys.stdin.readline().split()) #마을수==학생수, 도로수, start

G = [[] for _ in range(N+1)]
for i in range(M):
    v1, v2, t = map(int, sys.stdin.readline().split())
    G[v1].append((v2, t))


def dijkstra(start, end):
    h = []
    heapq.heappush(h, (0, start))
    visited = [0]*(N+1)
    road = [INF]*(N+1)
    road[start] = 0

    while h:
        t, v = heapq.heappop(h)
        if v == end:
            return road[end]
        for temp_v, temp_t in G[v]:
            if not visited[temp_v]:
                if road[temp_v] > t+temp_t:
                    road[temp_v]=t+temp_t
                    heapq.heappush(h, (road[temp_v], temp_v))
        visited[v] = 1

max = 0 
for i in range(1, N+1):
    temp = 0
    if i != X:
        temp += dijkstra(i, X)
        temp += dijkstra(X, i)
        if temp > max:
            max = temp

print(max)