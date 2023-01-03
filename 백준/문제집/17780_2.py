'''
제일 밑에 있는 말이 있는 위치를 map에 표시하는 이차원 배열을 따로 두는 방법

'''
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

G = []
for i in range(N):
    G.append(list(map(int, sys.stdin.readline().split())))

h_G = [[[] for _ in range(N)] for _ in range(N)]
h = [] 
for i in range(K):
    h.append(list(map(int, sys.stdin.readline().split())))
    h_G[h[i][0]-1][h[i][1]-1].append(i)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
change_dir = {1: 2, 2: 1, 3: 4, 4: 3}

count = 0
check = 0
while count <= 1000:
    count += 1
    for i in range(K):
        if h_G[h[i][0]-1][h[i][1]-1][0] != i:
            continue
        row = h[i][0] + dx[h[i][2]-1]
        col = h[i][1] + dy[h[i][2]-1]
        if row-1 < 0 or row-1 >= N or col-1 < 0 or col-1 >= N or G[row-1][col-1] == 2:
            h[i][2] = change_dir[h[i][2]]
            row = h[i][0] + dx[h[i][2]-1]
            col = h[i][1] + dy[h[i][2]-1]

        if 0 <= row-1 < N and 0 <= col-1 < N and G[row-1][col-1] != 2:
            if G[row-1][col-1] == 1:
                temp = h_G[h[i][0]-1][h[i][1]-1][-1::-1]
            else:
                temp = h_G[h[i][0]-1][h[i][1]-1]
            h_G[h[i][0]-1][h[i][1]-1] = []

            h_G[row-1][col-1].extend(temp)

            for j in temp:
                h[j][0] = row
                h[j][1] = col
            if len(h_G[row-1][col-1]) >= 4:
                check = 1
                break
    if check == 1:
        break

if count >= 1000:
    print("-1")
else:
    print(count)