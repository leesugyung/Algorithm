from collections import deque

def bfs(i,j):
    dx =[-1,0,+1,0]
    dy =[0,+1,0,-1]

    block, rainbow = [], []

    queue = deque()
    queue.append([i,j])
    block.append([i,j])

    while queue:
        cx, cy = queue.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if nx<0 or ny<0 or nx>=N or ny>=N: 
                continue
            if blocks[nx][ny] == -1:
                #검정 블록이면 패스
                continue
            if visited[nx][ny] == True:
                continue

            elif blocks[nx][ny] == 0 :
                #무지개 블록이라면 그룹에 추가
                queue.append([nx,ny])
                visited[nx][ny] = True #그룹 블록 체크
                rainbow.append([nx,ny])
            elif blocks[nx][ny] == blocks[i][j]:
                #숫자가 같은(색깔이 같은) 일반 블록이라면 블록그룹에 추가
                queue.append([nx,ny])
                visited[nx][ny] = True  #그룹 블록 체크, 일반 블록 방문처리
                block.append([nx,ny])

    for x, y in rainbow:
        visited[x][y] = False
    
    return [len(rainbow + block), len(rainbow), i, j, block+rainbow]  #이때, 기준 행과 열 i,j을 따로 주지 않고 블록 전체 리스트 [block+rainbow(행,열)]만 줘도 됨 -> 블록 전체 리스트 [block+rainbow(행,열)]의 [0]index가 어차피 제일 먼저 삽입된 일반블록이므로 기준행,기준열로 구성됨. 따라서 자동으로 이 원소를 기준으로 정렬해주기 때문이다.

def remove(rm):
    for x,y in rm:  # 리스트: [x,y]
        blocks[x][y] = -2


# 틀린 gravity 함수 (처음 작성한거)
# gravity에서 실수해서 87%에서 계속 테스트케이스 실패했다.
# 이게 틀린 gravity인데 , 53번째 줄에 if 0<=blocks[r][c]로 하면 되는데, if 0<=blocks[r][c]<=N 으로 하면 틀렸다고 그런다.
# 처음에는 인덱스 설정을 잘못한줄 알았더니, 알고보니 N과 M을 헷갈렸던 것이었다. N은 행,열개수이고 M이 일반블록번호를 나타내는것임..
# 결론 : N과 M 조건을 잘 보자 -> 이거 땜에 틀린거!!! ㅡㅡ 
# def gravity():
#     for c in range(0,N,1):
#         for r in range(N-1,-1,-1):
#             if 0 <= blocks[r][c] <= N:     #N을 M으로 바꾸면 정답임
#                 move_r = r
#                 while True:
#                     if move_r+1 == N or blocks[move_r+1][c] != -2 :
#                         break
#                     blocks[move_r+1][c] = blocks[move_r][c]
#                     blocks[move_r][c] = -2
#                     move_r += 1


# 정답 gravity 코드 이거 참고해서 풀었음
# def gravity():
#     for c in range(0,N,1):
#         for r in range(N-2,-1,-1):
#             if 0 <= blocks[r][c]:
#                 move_r = r
#                 while True:
#                     if 0<=move_r+1<N and blocks[move_r+1][c] == -2: 
#                         blocks[move_r+1][c] = blocks[move_r][c]
#                         blocks[move_r][c] = -2
#                         move_r += 1
#                     else:
#                         break


# 최종 gravity 함수:  gravity에서 제일 밑바닥 N-1번째 행은 떨어트릴 필요가 없으므로 체크안해도됨.
#      근데 나는 N-1부터 시작하게 했는데, 만약 제일 밑바닥 행이 선택됐을 경우 다음 행을 체크해줄 필요 없으므로 N-2로 하는게 맞음
#      따라서 N-2부터 시작하고, 다음행이 N이 넘으면 멈추는 조건을 == 이 아니라 >=라고 해서 좀더 실수를 줄이도록 한다.
def gravity():
    for c in range(0,N,1):
        for r in range(N-2,-1,-1):
            if 0 <= blocks[r][c] <= M:
                move_r = r
                while True:
                    if move_r+1 >= N or blocks[move_r+1][c] != -2 :
                        break
                    blocks[move_r+1][c] = blocks[move_r][c]
                    blocks[move_r][c] = -2
                    move_r += 1


def rotate():
    temp = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            temp[N-1-c][r] = blocks[r][c]
    return temp



#메인함수 시작
blocks = []   #블록 정보 저장하는 리스트
N, M = map(int,input().split())
for i in range(N):
    blocks.append(list(map(int,input().split())))
visited = [[False]*N for _ in range(N)]  #블록 방문 여부 저장하는 리스트
score = 0  #점수

while True: 
    group = []   #블록그룹을 저장하는 리스트 [일반블록+무지개블록 총개수, 무지개블록개수, 기준행, 기준열, 전체 블록(일반블록+무지개) 좌표 ] while문 실행마다 블록그룹은 새로 찾아야 하므로, 초기화가 필수다
    g = []
    visited = [[False]*N for _ in range(N)]  #while문 실행마다 블록그룹은 새로 찾아야 하므로, 방문 배열 역시 초기화 필수다


    #크기가 가장 큰 블록 그룹을 찾음
    for i in range(N):
        for j in range(N):
            if 0 < blocks[i][j] and visited[i][j] == False:
                #방문안한 일반 블록일 경우 그룹 찾는 bfs 수행
                visited[i][j] = True
                g = bfs(i,j)
                if g[0] >= 2: 
                    group.append(g)

    #group = sorted(group, key = lambda x: (-x[0],-x[1],-x[2],-x[3]))
    group.sort(reverse=True)  #블록그룹을 전체블록개수-> 무지개블록개수-> 기준행 -> 기준열 큰순대로 정렬

    if len(group) == 0:         #만약 이렇게 bfs해서 탐색했는데, 리스트에 블록그룹이 하나도 없다면 중단
        break
    
    #선택된 가장 큰 블록 그룹(group[0] -> 정렬했으니까 제일 앞에 인덱스)을 맵에서 제거. score 더해줌
    remove(group[0][4])
    score += group[0][0]**2

    #격자에 중력 작용
    gravity()


    #격자 반시계 회전
    blocks = rotate()


    #격자에 중력 작용
    gravity()




print(score)
