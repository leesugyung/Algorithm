'''
아이디어 자체는 근처까지 갔지만,
구현을 전혀 못한 문제

2차원 배열로 풀 생각을 어떻게 하지?
list[자리수][끝에오는숫자]

나는 일차원 배열 여러개로 이리저리 하려고했음 
막 copy하고 난리날뻔~~
'''

import sys

N = int(sys.stdin.readline())

a = [[0]*10 for _ in range(N+1)]

for i in range(1, 10):
    a[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            a[i][j] = a[i-1][1]
        elif j == 9:
            a[i][j] = a[i-1][8]
        else:
            a[i][j] = a[i-1][j-1]+a[i-1][j+1]

count = sum(a[N])

print(count%1000000000)