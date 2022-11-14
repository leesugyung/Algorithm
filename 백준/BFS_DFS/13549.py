'''
뭔가 풀긴 풀었는데 찝-찝한 기분

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

cost = [sys.maxsize]*100001
visited = [0]*100001

def bfs(n):
    d = deque([n])
    cost[n] = 0
    visited[n] = 0
    
    while d:
        x = d.popleft()
        if x == K:
            break

        for i in [x+1, x-1]:
            if 0<=i<=100000:
                if cost[i] > cost[x]+1:
                    cost[i] = cost[x]+1
                    d.append(i)
        if 0<=x*2<=100000:
            if visited[x*2] == 0:
                if cost[x*2] > cost[x]:
                    cost[x*2] = cost[x]
                    d.append(x*2)
                    visited[x*2] = 1
    print(cost[K])

bfs(N)
'''

import sys
from collections import deque


# 0 - 1 bfs 탐색
def bfs():
    graph = [-1] * 100001
    graph[n] = 0
    queue = deque([n])

    while queue:
        target = queue.popleft()

        # 동생의 위치에 도달했다면 리턴
        if target == k:
            return graph[target]

        # 반복문을 통해 3가지 이동의 경우를 확인
        for i in (target + 1, target - 1, target * 2):

            # 이동하는 곳이 범위 내에 있고 이동하지 않았다면 이동
            if 0 <= i <= 100000 and graph[i] == -1:
                # 순간이동이라면
                if i == target * 2:
                    graph[i] = graph[target] # 0초 갱신
                    queue.appendleft(i) # 순간이동이기에 먼저 탐색

                else:
                    graph[i] = graph[target] + 1
                    queue.append(i)


n, k = map(int, sys.stdin.readline().split())
print(bfs())