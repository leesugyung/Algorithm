'''
[문제 정리]
일반블록: M가지 색, 검은색 블록: -1, 무지개 블록: 0
|r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸을 인접한 칸 == 상하좌우

블록 그룹(>=2) -> 일반 블록 must 1개 이상 and 같은 색, 검은색 ㄴㄴ, 무지개 상관 ㄴㄴ
                + 연결되어있어야 하고 
    기준 블록: 일반 블록 중 행이 가장 작은 블록 (다음은 열)

오토 플레이 기능 반복 :
1. 크기 가장 큰 블록 그룹 찾기 (여러개? 무지개 많 -> 기준 블록 행 큼 -> 열)
2. 찾은 블록 그룹의 블록 제거 and 점수 = 블록그룹의 블록 수의 제곱
3. 벽 만날 때 까지 밑으로 내리기 (검은 블록 제외)
4. 반시계방향 회전
5. 벽 만날 때 까지 밑으로 내리기 (검은 블록 제외)

점수 총합

[풀이 정리]
1. 블록과 블록에 대한 정보를 담아놓는 것을 리스트로 해서 역정렬을 하여 큰 블록을 알아낸다.
그리고 이때 rainbow와 normal block을 따로 담아놓고 리턴할 때 normal block을 앞으로 해야하는데 sort할 때 기준 블록의 행과 열이 큰 것이 앞에 가게 하기 위함임

* 나는 deque로 하면 시간이 적게 걸릴 것 같아 deque를 사용하고 싶었는데 그러면 index에 따른 접근이 안되므로 잘못된 생각이었음.
rainbow와 normal block을 따로 담아야 되는 것도 생각하지 못한 부분이었음.

2. BFS할 때는 rainbow과 normal block 두 블록 모두 방문표시를 해줘야 함 
반면, 메인 코드에서는 rainbow는 중복사용이 가능하므로 normal block에 대해서만 방문표시를 해야됨.

* 나는 메인 코드에서 rainbow에 대한 중복사용에 너무 중점을 둔 나머지 BFS에서의 rainbow의 방문 여부를 체크안해줌. 이렇게 되면 계속 돌게 될 것임.

3. 90도 반시계 회전을 zip으로 구현하기
a = list(zip(*a))[::-1]
a = [list(s) for s in a]

4. 중력
밑에서 부터 체크를 하고, 다음 행이 black이거나 벽일 때까지 계속 내려야 하므로 while을 사용해야 함
그리고 이걸 모든 열에 대해서 해줘야 하므로 이중포문+while로 처리해주면 됨.

5. zip() -> 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수.

ex)
a = list(zip([1, 2, 3], [4, 5, 6]))
b = list(zip("abc", "def"))

print(a)
print(b)

# 실행 결과
[(1, 4), (2, 5), (3, 6)]
[('a', 'd'), ('b', 'e'), ('c', 'f')]

1. 시계 방향으로 회전
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist[::-1])))

2. 반시계 방향으로 회전
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))[::-1]

6. arr[A:B:C] = index A부터 index B까지 C의 간격으로 배열을 만들어라
arr[::-1] = 역순으로

'''

import sys
from collections import deque

def BFS(color, i, j):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((i, j))

    count = 1
    rainbow_count = 0

    rainbow = deque()
    normal_block = deque()
    normal_block.append((i, j))

    temp_visited = [[False]*N for _ in range(N)]
    temp_visited[i][j] = True

    while q:
         x, y = q.popleft()
         for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                continue
            if not temp_visited[nx][ny] and G[nx][ny] == 0:
                q.append((nx, ny))
                rainbow.append((nx, ny))
                rainbow_count += 1
                count += 1
                temp_visited[nx][ny] = True
            elif not temp_visited[nx][ny] and not visited[nx][ny] and G[nx][ny] == color:
                q.append((nx, ny))
                normal_block.append((nx, ny))
                count += 1
                visited[nx][ny]=True
                temp_visited[nx][ny] = True
        

    return [count, rainbow_count, normal_block+rainbow]
    
def delete(count, max_group):
    for i in range(count):
        x, y = max_group[i]
        G[x][y] = -2

def gravity(G):
    for i in range(N): #열
        for j in range(N-2, -1, -1): #행
            if G[j][i] < 0:
                continue
            r = j
            while r < N-1:
                if G[r+1][i] != -2:
                    break
                G[r+1][i]=G[r][i]
                G[r][i] = -2
                r += 1

'''
def rotate(G):
    new_G = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_G[i][j] = G[j][N-1-i]
    return new_G
'''

def rotate(G):
    G = list(map(list,zip(*G)))[::-1]
    return G


#메인 코드 
N, M = map(int, sys.stdin.readline().rstrip().split())

G = [[] for _ in range(N)]
for i in range(N):
    G[i] = list(map(int, sys.stdin.readline().rstrip().split()))

score = 0

while True:
    visited = [[False]*N for _ in range(N)]
    groups = []

    for j in range(N):
            for k in range(N):
                if G[j][k] > 0 and visited[j][k]==False:
                    visited[j][k] = True
                    block_info = BFS(G[j][k], j, k)
                    if block_info[0] > 1:
                        groups.append(block_info)
    if not groups:
        break

    groups.sort(reverse=True)
    score += groups[0][0]**2    

    delete(groups[0][0], groups[0][2])
    gravity(G)
    G = rotate(G)
    gravity(G)

print(score)