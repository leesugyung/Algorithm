import sys
from collections import deque

M, N = map(int, sys.stdin.readline().rstrip().split()) #가로칸(열), 세로칸(행)
G = [[] for _ in range(N)]

tomato = 0
marking = deque()
check = 0
result = -1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    G[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(M):
        if G[i][j] == 0:
            tomato += 1
        elif G[i][j] == 1:
            marking.append((i,j))

while marking:
    x, y = marking.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
            continue
        if G[nx][ny] != 0:
            continue
        G[nx][ny] = G[x][y] + 1
        if result < G[nx][ny]:
            result = G[nx][ny]
        marking.append((nx, ny))
        check += 1

if check != tomato:
    print(-1)
elif tomato == 0:
    print(0)
else:
    print(result-1)