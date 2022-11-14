import sys
import heapq
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

bus = [[] for _ in range(n+1)]
for i in range(m):
    x, y, w = map(int, sys.stdin.readline().split())
    bus[x].append((y, w))

start, end = map(int, sys.stdin.readline().split())

road = [[sys.maxsize, -1] for _ in range(n+1)] #최단경로, 이전에 거치는 노드
h = []
heapq.heappush(h, (0, start))
road[start][0] = 0

visited = [0]*(n+1)

while h:
    w, x = heapq.heappop(h)
    if x == end:
        break
    for temp_x, temp_w in bus[x]:
        if visited[temp_x] == 0: #처음 방문
            if road[temp_x][0] > temp_w+w:
                road[temp_x][0] = temp_w+w
                road[temp_x][1] = x
                heapq.heappush(h, (road[temp_x][0], temp_x))
    visited[x] = 1

print(road[end][0])
count = 0
temp = end
result = deque()
while temp != -1:
    result.appendleft(temp)
    temp = road[temp][1]

print(len(result))
for i in result:
    print(i, end=" ")