'''
물고기: 번호(1<=x<=16, 중복x)와 방향(상하좌우, 대각선)

상어가 들어와 물고기를 먹는다.

맨 처음 (0,0)의 물고기 먹음
상어의 방향 == 물고기의 방향

물고기 이동(한 칸)
번호가 작은 물고기부터 순서대로 이동
이동가능: 빈 칸 or 다른 물고기 / 이동불가능: 상어 or 벽

원래방향~이동할 수 있는 칸을 향할 때까지 45도 반시계회전
이동할 수 있는 칸이 없으면 이동x
if 물고기가 다른 물고기가 있는 칸으로 이동? 서로 위치를 바꿈

물고기 이동 종료 -> 상어 이동(여러 개의 칸 이동 가능, 방향에 있는 칸들로 이동)
이동 시 그 칸의 물고기 먹으며 그 물고기의 방향 get
이동 중에는 물고기를 먹지 않음
물고기 없는 칸은 이동할 수 없음.

더이상 상어가 이동할 수 있는 칸x? 종료

output : 상어가 먹을 수 있는 물고기 번호의 합의 최댓값

****************<이번 문제에서 어려웠던 점>*****************
1. 재귀를 하여 G가 바뀌므로 deepcopy를 해줘야 한다는 점이 어려웠고, 어디까지 임시로 카피한 리스트를 사용해야될 지 헷갈렸음.

2.다른 코드를 보지 않고 성공하긴 했음.
but, 예시 결과 2개가 다른 값이 나오거나 재귀가 너무 많이 된다고 에러가 떴음.

첫 번째 문제:
처음에는 빈 칸일 땐 그냥 냅다 거기에 넣기만 하였음.
그러다보니, 빈 칸은 바뀌지 않고 이사온 물고기를 가리켰을 거고 그러다 보니 재귀가 계속해서 일어나는 이슈가 있었음.
그래서 빈 칸의 위치도 바꿔주는 식으로 무한 재귀는 해결할 수 있었음.

두 번째 문제:
상어가 먹어서 빈 칸이 되면 그 칸의 번호를 -1로 바꿔주는 방법으로 코드를 작성했음.
그런데, 그렇게 되면 물고기가 빈 칸으로 이동했을 때 
빈 칸의 위치를 바꾸려고 해도 번호가 -1이므로 fish_location[-1], 즉 맨 뒤만 괜히 바뀌게 됨.
그리고 빈 칸은 그대로 이사 온 물고기를 가리킴.
그래서 번호는 그대로 두고 방향을 -1로 바꿔주는 방법으로 해결하였음.

=> 결론: 포문을 돌려가면서 순서대로 물고기가 돌아갈 수 있도록 하는 것이 시간이 오래걸릴 것 같아
fish_location이라는 위치 저장 리스트를 만든 거였는데 어차피 그 리스트도 괜히 deepcopy를 해야되서 시간이 오래걸림
그리고 위치도 계속 바꿔야하는 것 때문에 일어나지 않아도 될 문제들이 계속 생겼고, 그로 인해 많은 고생을 했음.


****************<파이썬이 충격적이었던 점>*****************
1. temp없이 냅다 교환된다.
fish_location[G[x][y][0]],fish_location[i]=fish_location[i],fish_location[G[x][y][0]]

2. 일일히 대입해줄 필요없다.
x = fish_location[i][0]
y = fish_location[i][1] 대신

x, y = fish_location[i] 이 가능하다.

아직까지 파이썬을 못쓰는게 너무 보임.
'''
import sys
from copy import deepcopy

G = [[] for _ in range(4)]
fish_location = [[0,0] for _ in range(17)]

for i in range(4):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(4):
        G[i].append([temp[j*2],temp[j*2+1]])
        fish_location[temp[j*2]][0]=i
        fish_location[temp[j*2]][1]=j

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def fish_move(shark_x, shark_y, G, fish_location):
    for i in range(1, 17):
        x = fish_location[i][0]
        y = fish_location[i][1]
        dir = G[x][y][1]-1
        if G[x][y][1]==-1:
            continue
        for j in range(8):
            nx = x+dx[(dir+j)%8]
            ny = y+dy[(dir+j)%8]
            if nx < 0 or nx > 3 or ny < 0 or ny > 3 or (shark_x==nx and shark_y==ny):
                continue
            G[nx][ny], G[x][y] = [i, (dir+j)%8+1], G[nx][ny]
            fish_location[G[x][y][0]],fish_location[i]=fish_location[i],fish_location[G[x][y][0]]
            break
            

def shark_move(shark_x, shark_y, score, graph, fish):
    global max

    temp_G = deepcopy(graph)
    temp_fish = deepcopy(fish)

    score+= temp_G[shark_x][shark_y][0]
    shark_dir = temp_G[shark_x][shark_y][1]
    temp_G[shark_x][shark_y][1] = -1

    fish_move(shark_x, shark_y, temp_G, temp_fish)
    
    for i in range(1, 4):
        nx = shark_x+dx[shark_dir-1]*i
        ny = shark_y+dy[shark_dir-1]*i
        if nx < 0 or nx > 3 or ny < 0 or ny > 3:
            if max < score:
                max = score
            return
        if temp_G[nx][ny][1] == -1:
            if i == 3:
                return
            continue
        shark_move(nx, ny, score, temp_G, temp_fish)

max = 0
shark_move(0, 0, 0, G, fish_location)

print(max)