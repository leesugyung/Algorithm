import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
G = [[] for _ in range(N)]

for i in range(0, N):
    G[i] = list(map(int, sys.stdin.readline().rstrip()))


nowR, nowC, checkR, checkC = 0, 0, 0, 0
direction = [[1, 0],[0, 1], [-1, 0],[0,-1]] #[오른쪽, 아래, 위, 왼쪽]

q = deque()
q.append((0,0))

while q:
    nowR, nowC = q.popleft()

    for i in range(0, 4):
        checkR = nowR + direction[i][0]
        checkC = nowC + direction[i][1]
        if checkR < 0 or checkR > N-1 or checkC < 0 or checkC > M-1:
            continue
        if G[checkR][checkC] != 1:
            continue
        q.append((checkR, checkC))
        G[checkR][checkC] = G[nowR][nowC] + 1

print(G[N-1][M-1])