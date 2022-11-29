'''
어떤 수보다 작은 자연수의 곱이 몇 개인지를 못 구함,,,

행으로 나눈 몫

'''

import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

start = 1
end = k

while start<=end:
    mid = (start+end)//2
    temp = 0
    for i in range(1, N+1):
        temp += min(mid//i, N)
    if temp >= k:
        end = mid-1
    else:
        start = mid+1

print(start)