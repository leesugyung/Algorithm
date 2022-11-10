import sys
import heapq

INF = sys.maxsize

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

G = [[] for _ in range(N+1)]
for i in range(1, M+1):
    v1, v2, w = map(int, sys.stdin.readline().split())
    G[v1].append((v2, w))

start, end = map(int, sys.stdin.readline().split())

h = []
heapq.heappush(h, (0, start))
road = [INF]*(N+1)
road[start] = 0

visited = [0]*(N+1)

def dijkstra():
    while h:
        w, v = heapq.heappop(h)
        if v == end:
            return road[end]
        for temp_v, temp_w in G[v]:
            if not visited[temp_v]:
                if road[temp_v] > w + temp_w:
                    road[temp_v] = w + temp_w
                    heapq.heappush(h, (road[temp_v], temp_v))
        visited[v] = 1

print(dijkstra())                