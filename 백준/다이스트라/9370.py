import sys
import heapq

T = int(sys.stdin.readline())

def dijkstra(start, end):
    h = []
    heapq.heappush(h, (0, start))
    visited = [0]*(n+1)
    weight = [sys.maxsize]*(n+1)
    weight[start] = 0

    while h:
        w, x = heapq.heappop(h)
        if x == end:
            return weight[end]
        for temp_x, temp_w in road[x]:
            if visited[temp_x] == 0:
                if weight[temp_x] > w+temp_w:
                    weight[temp_x] = w+temp_w
                    heapq.heappush(h, (weight[temp_x], temp_x))
        visited[x] = 1

    return weight[end]

for i in range(T):
    n, m, t = map(int, sys.stdin.readline().rstrip().split()) #교차로, 도로, 목적지 후보 개수
    s, g, h = map(int, sys.stdin.readline().rstrip().split()) #c출발지, 노드 사이 도로 지나감
    
    road = [[] for _ in range(n+1)]
    for j in range(m):
        a, b, d = map(int, sys.stdin.readline().rstrip().split())
        road[a].append((b, d))
        road[b].append((a, d))

    c = []
    for j in range(t):
        temp = int(sys.stdin.readline())
        if dijkstra(s,temp) == min(dijkstra(s,g)+dijkstra(h, temp), dijkstra(s,h)+dijkstra(g, temp))+dijkstra(g,h):
            c.append(temp)

    c.sort()
    for i in c:
        print(i, end=" ")
    print()