import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

G = []
for i in range(N):
    G.append(list(map(int, sys.stdin.readline().split())))

h = [] 
for i in range(K):
    h.append(list(map(int, sys.stdin.readline().split())))
    h[i].append(-1)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

result = 0

stack = []
m = -1
check = 0

while(1):
    if check == 1 or result >= 1000:
        break
    result += 1
    for i in range(K):
        if h[i][3] == -1:  #아직 쌓이지않음.
            row = h[i][0] + dx[h[i][2]-1]
            col = h[i][1] + dy[h[i][2]-1]
            if row-1 < 0 or row-1 >= N or col-1 < 0 or col-1 >= N or G[row-1][col-1] == 2: #파란색이거나 범위를 넘음
                if h[i][2] == 1:
                    h[i][2] = 2
                elif h[i][2] == 2:
                    h[i][2] = 1
                elif h[i][2] == 3:
                    h[i][2] = 4
                else:
                    h[i][2] = 3

                row = h[i][0] + dx[h[i][2]-1]
                col = h[i][1] + dy[h[i][2]-1]
                

            if  0 <= row-1 < N and 0 <= col-1 < N and G[row-1][col-1] != 2: #흰색 or 빨간색
                for j in range(K):
                    if j != i and h[j][0] == row and h[j][1] == col:
                        if h[j][3] == -1:
                            d = deque([0, j, i]) #d[0] = reverse여부
                            stack.append(d)
                            size = len(stack) #stack의 index 넣기
                            h[j][3] = size-1
                            h[i][3] = size-1
                            if m < 2:
                                m = 2
                        else: 
                            if stack[h[j][3]][0] == 0:
                                stack[h[j][3]].append(i)
                            else:
                                stack[h[j][3]].appendleft(1)
                                stack[h[j][3]][1] = i
                            h[i][3] = h[j][3]
                            size = len(stack[h[j][3]])-1
                            if m < size:
                                m = size
                        break
                h[i][0] = row
                h[i][1] = col
        else: #쌓임
            index = h[i][3]
            if stack[index][0] == 0:
                bottom = stack[index][1]
            else:
                bottom = stack[index][-1]
            if bottom == i:
                row = h[i][0] + dx[h[i][2]-1]
                col = h[i][1] + dy[h[i][2]-1]
                if row-1 < 0 or row-1 >= N or col-1 < 0 or col-1 >= N or G[row-1][col-1] == 2: #파란색이거나 범위를 넘음
                    if h[i][2] == 1:
                        h[i][2] = 2
                    elif h[i][2] == 2:
                        h[i][2] = 1
                    elif h[i][2] == 3:
                        h[i][2] = 4
                    else:
                        h[i][2] = 3

                    row = h[i][0] + dx[h[i][2]-1]
                    col = h[i][1] + dy[h[i][2]-1]

                if 0 <= row-1 < N and 0 <= col-1 < N and G[row-1][col-1] != 2 : #흰색이거나 빨간색
                    if G[row-1][col-1] == 1: #빨간색이면 reverse해주기
                        if stack[index][0] == 0:
                            stack[index][0] = 1
                        else:
                            stack[index][0] = 0

                    for k in range(1, len(stack[index])):
                        h[stack[index][k]][0] = row
                        h[stack[index][k]][1] = col

                    for j in range(K):
                        if j != i and h[j][0] == row and h[j][1] == col and h[j][3] != index:
                            if h[j][3] == -1:
                                if stack[index][0] == 0:
                                    stack[index].appendleft(0)
                                    stack[index][1] = j
                                else:
                                    stack[index].append(j)
                                h[j][3] = index
                                size = len(stack[index])-1
                                if m < size:
                                    m = size
                            else: 
                                if stack[h[j][3]][0] == 0:
                                    if stack[index][0] == 0:
                                        for k in range(1, len(stack[index])):
                                            stack[h[j][3]].append(stack[index][k])
                                            h[stack[index][k]][3] = h[j][3]
                                    else:
                                        for k in range(len(stack[index])-1, 0, -1):
                                            stack[h[j][3]].append(stack[index][k])
                                            h[stack[index][k]][3] = h[j][3]
                                else:
                                    if stack[index][0] == 0:
                                        for k in range(1, len(stack[index])):
                                            stack[h[j][3]].appendleft(1)
                                            stack[h[j][3]][1] = stack[index][k]
                                            h[stack[index][k]][3] = h[j][3]
                                    else:
                                        for k in range(len(stack[index])-1, 0, -1):
                                            stack[h[j][3]].appendleft(1)
                                            stack[h[j][3]][1] = stack[index][k]
                                            h[stack[index][k]][3] = h[j][3]
                                break

                    size = len(stack[h[i][3]])-1
                    if m < size:
                        m = size
        if m >= 4:
            check = 1
            break

if result >= 1000:
    print(-1)
else:
    print(result)