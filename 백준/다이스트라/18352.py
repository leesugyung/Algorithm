import sys
import heapq

N, M, K, X = map(int, sys.stdin.readline().split())


G = [[] for _ in range(N+1)]
result = []

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    G[x].append(y)

def dijstra(start):
    h = []
    heapq.heappush(h, (0, start))
    road = [sys.maxsize]*(N+1)
    visited = [0]*(N+1)
    road[start] = 0
    check = 0
   
    while h:
        w, n = heapq.heappop(h)
        for i in G[n]:
            if visited[i] == 0:
                if road[i] > w + 1:
                    road[i] = w+1
                    if road[i] == K:
                        heapq.heappush(result, i)
                    elif road[i] > K:
                        check = 1
                    heapq.heappush(h, (road[i], i))
        if check != 0:
            break
        visited[n] = 1

dijstra(X)
if not result:
    print(-1)
else:
    while result:
        print(heapq.heappop(result))