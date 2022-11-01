'''
대실패~!!
경우를 나눠서

1) 해당 순서의 포도주를 마시는 경우
    i) 이전 순서의 포도주를 마신 경우
    ii) 이전 순서의 포도주를 마시지 않은 경우
2) 해당 순서의 포도주를 마시지 않은 경우

d[i] : i번째 포도주까지 최대로 마신 포도주의 양
-> i번째 포도주 + i+2번째까지 마신 양
   i, i-1번째 포도주를 마시고 i-3번째까지 마신 양
   i번째를 마시지 않은 경우(=i-1번째 포도주까지 마신 양)


'''

import sys

N = int(sys.stdin.readline())

wine = [0]
for i in range(N):
    wine.append(int(sys.stdin.readline()))

d = [0]*(N+1)
d[1] = wine[1]
if N>1:
    d[2] = wine[1] + wine[2]

for i in range(3, N+1):
    d[i] = max(d[i-1], d[i-2]+wine[i], d[i-3]+wine[i-1]+wine[i])

print(d[N])