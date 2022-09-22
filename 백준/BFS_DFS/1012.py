import sys
from collections import deque

T = int(sys.stdin.readline())

def BFS(x, y, G):
    dx = [-1, 1, 0 ,0] #상하좌우
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((x,y))
    G[x][y] = 0

    while q:
        nx, ny = q.popleft()
        for i in range(4):
            a = nx + dx[i]
            b = ny + dy[i]
            if a < 0 or a > N-1 or b < 0 or b > M-1:
                continue
            if G[a][b] == 0:
                continue
            G[a][b] = 0
            q.append((a,b))

for i in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    G = [[0]*M for _ in range(N)]
    for i in range(K):
        y, x = map(int, sys.stdin.readline().rstrip().split())
        G[x][y] = 1
    
    check = 0
    for i in range(N):
        for j in range(M):
            if G[i][j] == 1:
                check += 1
                BFS(i,j,G)
    print(check)