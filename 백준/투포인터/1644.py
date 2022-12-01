'''
에라토스테네스의 체? 소수를 판별하는 알고리즘, 소수들을 대량으로 빠르고 정확하게 구한다.
어떤 수의 소수의 여부를 확인할 때 -> 특정한 숫자의 제곱근까지만 약수의 여부 검증! => O(N^1/2)의 시간 복잡도

에라토스테네스의 체는 가장 먼저 소수를 판별할 범위만큼 배열을 할당하여, 해당하는 값을 넣어주고, 이후에 하나씩 지워나가는 방법을 이용한다.

1. 배열을 생성하여 초기화한다.
2. 2부터 시작해서 특정 수의 배수에 해당하는 수를 모두 지운다.(지울 때 자기자신은 지우지 않고, 이미 지워진 수는 건너뛴다.)
3. 2부터 시작하여 남아있는 수를 모두 출력한다.
'''
'''
import sys
from collections import deque

N = int(sys.stdin.readline())

prime_num = [True]*(N+1)
prime_list = deque()

for i in range(2, N+1):
    if not prime_num[i]: continue
    else: prime_list.append(i)

    for j in range(2*i, N+1, i):
        prime_num[j] = False    

s_index, e_index = 0, 0
temp = 0
count = 0

while True:
    if temp > N:
        if s_index > e_index:
            break
        temp -= prime_list[s_index]
        s_index += 1

    elif temp < N:
        if e_index >= len(prime_list):
            break
        temp += prime_list[e_index]
        e_index += 1

    else:
        count += 1
        if e_index >= len(prime_list):
            break
        temp += prime_list[e_index]
        e_index += 1

print(count)
'''

import math

N = int(input())

a = [False, False] + [True] * (N-1)
prime_num = []

for i in range(2, N+1):
    if a[i]:
        prime_num.append(i)
        for j in range(2*i, N+1, i):
            a[j] = False

answer = 0
start = 0
end = 0
while end <= len(prime_num):
    temp_sum = sum(prime_num[start:end])
    if temp_sum == N:
        answer += 1
        end += 1
    elif temp_sum < N:
        end += 1
    else:
        start += 1

print(answer)