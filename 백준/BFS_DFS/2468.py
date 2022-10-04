'''
핵심 - 안전한 영역의 최대 개수, 아무 지역도 물에 잠기지 않을 수 있다.
최고 높이까지 오면 모두 잠기기 때문에 최고 높이-1 까지만 계산한다.
'''

import sys
from collections import deque

def BFS(h):
    visited = [[False]*N for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1 , 1]
    safe = 0

    for i in range(N):
        for j in range(N):
            if G[i][j] > h and not visited[i][j]:
                safe += 1
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                            continue
                        if G[nx][ny] <= h or visited[nx][ny]:
                            continue
                        visited[nx][ny] = True
                        q.append((nx,ny))

    return safe

N = int(sys.stdin.readline())
G = [[]*N for _ in range(N)]
min_v = 101
max_v = 1
ans = 1

for i in range(N):
    G[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(N):
        if min_v > G[i][j]:
            min_v = G[i][j]
        if max_v < G[i][j]:
            max_v = G[i][j]

for i in range(min_v, max_v):
    check = BFS(i)
    if ans < check:
        ans = check

print(ans)