'''
너무너무 어려웠다 ㅠ 어캄?
엄청 많이 시도해서 엄청 많이 틀림 ^^
'''

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

#최단경로, 방문횟수
visited = [[-1, 0] for _ in range(100001)]

def bfs(n):
    d = deque([n])
    visited[n][0] = 0
    visited[n][1] = 1
    
    while d:
        x = d.popleft()
        for i in [x*2, x+1, x-1]:
            if 0<=i<=100000:
                if visited[i][0]==-1:
                    visited[i][0] = visited[x][0]+1
                    visited[i][1] = visited[x][1]
                    d.append(i)
                elif visited[i][0] == visited[x][0]+1:
                    visited[i][1] += visited[x][1]

bfs(N)
print(visited[K][0])
print(visited[K][1])