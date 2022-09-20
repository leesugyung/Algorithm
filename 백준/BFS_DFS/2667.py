import sys
from collections import deque

N = int(sys.stdin.readline())

G = [[] for _ in range(N)]

for i in range(N):
    G[i] = list(map(int, sys.stdin.readline().rstrip()))

dx = [-1, 1, 0, 0] #상하좌우
dy = [0, 0, -1, 1]

def bfs(G, i, j):
    q = deque()
    q.append((i,j))
    cnt = 1
    G[i][j]=0
    
    while q:
        nx, ny = q.popleft()
        for i in range(4):
            x = nx + dx[i]
            y = ny + dy[i]
            if x < 0 or x > N-1 or y < 0 or y > N-1:
                continue
            if G[x][y] == 1:
                q.append((x, y))
                cnt +=1
                G[x][y] = 0
    return cnt

count = [bfs(G, i, j) for i in range(N) for j in range(N) if G[i][j]==1]

count.sort()
print(len(count))
for i in range(len(count)):
    print(count[i])
        