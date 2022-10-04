'''
벽만들기 -> 안전영역 크기 재기
Deep Copy(원본 데이터 보존)
1. copy 모듈의 deepcopy()함수
2. list slicing [:]

copy_list_a = copy.deepcopy(origin_list)    # deepcopy() function of copy module
copy_list_b = origin_list[:]                # slicing

<쓰임>
slicing이 deepcopy()함수보다 빠르다.
그러나 slicing은 리스트에서만 사용할 수 있지만, deepcopy()함수는 모든 타입의 변수를 복사할 수 있다.
또한, [:]로 리스트를 복사하는 건 nested list까지는 적용이 되지 않는다는 점


python3으로 제출 시 시간초과
-> 조합 사용!

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

def make_wall(count):
    if count == 3:
        BFS()
        return
    for i in range(N):
        for j in range(M):
            if G[i][j] == 0:
                G[i][j] = 1
                make_wall(count+1)
                G[i][j] = 0

result = 0
make_wall(0)

print(result)