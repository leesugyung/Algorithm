'''
#pypy로만 풀림

import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

e = 0
count = 0

for s in range(N):
    temp = 0
    e = s
    while e<N:
        temp += A[e]
        e+= 1
        if temp == M:
            count += 1
            break        
        elif temp > M:
            break

print(count)
'''

import sys 

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

s, e, count = 0, 0, 0
temp = A[e]

while True:
    if temp < M:
        e+=1
    elif temp > M:
        temp -= A[s]
        s+=1
        continue
    else:
        count += 1
        e+=1
    if s > e or e >= N:
        break
    temp+=A[e]

print(count)