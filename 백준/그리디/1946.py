'''
문제를 이해하기 어려웠던 문제
구현 자체는 쉬움
'''

import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    applicant = []
    for j in range(N):
        applicant.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
    applicant.sort()
    temp = applicant[0][1]
    cnt = 1
    for j in range(1, N):
        if temp > applicant[j][1]:
            cnt += 1
            temp = applicant[j][1]

    print(cnt)