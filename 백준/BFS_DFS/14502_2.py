'''
python3으로 제출 시 시간초과
-> 조합 사용!

2차원 배열에서 조합구하기 : 기본적인 방법은 조합과 유사하지만, 뽑고자하는 원소의 행과 열을 뽑는 방법
-> 나누기와 모듈러 연산 사용!

예시)
N M = 3 3
range(0, 9)

i: row col
0: 0 0 
1: 0 1
2: 0 2
3: 1 0
4: 1 1
5: 1 2
6: 2 0
7: 2 1
8: 2 2
'''

import sys
import copy
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
G = [[] for _ in range(N)]
q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0 , -1 ,1]

for i in range(N):
    G[i] = list(map(int, sys.stdin.readline().rstrip().split()))

def BFS():
    check = 0
    global result
    q = deque()
    for i in range(N):
        for j in range(M):
            if G[i][j] == 2:
                q.append((i, j))

    copyG = copy.deepcopy(G)

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
                continue
            if copyG[nx][ny] != 0:
                continue
            copyG[nx][ny] = 2
            q.append((nx, ny))

    for i in range(N):
        for j in range(M):
            if copyG[i][j] == 0:
                check += 1
    
    result = max(result, check)

def make_wall(start, count):
    if count == 3:
        BFS()
        return

    #조합
    for i in range(start, N*M):
        row = i // M #열의 길이로 나누면 행의 위치를 알 수 있습니다.
        col = i % M #열의 길이로 나머지 연산을 하면 열의 위치를 알 수 있습니다.
        if G[row][col] == 0:
            G[row][col] = 1
            make_wall(i, count+1)
            G[row][col] = 0

result = 0
make_wall(0, 0)

print(result)