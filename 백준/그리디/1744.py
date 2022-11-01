'''
문제를 잘못 이해해서 크게 낭패본 문제
같은 위치에 있는 수를 묶는 것은 불가능하다고 하길래 당연히 같은 숫자는 곱하기를 못하는줄;;

잘못 이해한 것을 알게 되고나선 쉬웠는데
1일때 예외처리해주어야 하는게 살짝 까다로웠다.
'''

import sys
import heapq

N = int(sys.stdin.readline())

minus = []
plus = []

for i in range(N):
    temp = int(sys.stdin.readline())
    if temp <= 0:
        heapq.heappush(minus, temp)
    else:
        heapq.heappush(plus, [-temp, temp])


sum = 0

for i in range(0, len(minus)-1, 2):
    x = heapq.heappop(minus)
    y = heapq.heappop(minus)
    sum += x*y
if minus:
    sum += heapq.heappop(minus)

for i in range(0, len(plus)-1, 2):
    x = heapq.heappop(plus)[1]
    y = heapq.heappop(plus)[1]
    if x == 1 or y == 1:
        sum += x+y
    else:
        sum += x*y
if plus:
    sum += heapq.heappop(plus)[1]
    

print(sum)