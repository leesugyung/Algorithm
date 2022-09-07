import sys

case = int(input())
output = []

def Print_Q(N, M, li):
    count = 0
    max_index = 0
    for i in range(0, N):
        l_max_index = li[max_index:].index(max(li[max_index:])) + max_index
        r_max_index = li[:max_index+1].index(max(li[:max_index+1]))
        if li[l_max_index] >= li[r_max_index]:
            max_index = l_max_index
        else:
            max_index = r_max_index
        if max_index == M :
            count += 1
            return count
        li[max_index] = 0
        count += 1
    return count

for i in range(0, case):
    N, M = map(int, sys.stdin.readline().split())
    li = list(map(int, sys.stdin.readline().split()))
    count = Print_Q(N, M, li)
    output.append(count)

for i in output:
    print(i)

"""
<deque VS list>

from collections import deque
deque.append(x) / deque.appendleft(x) / deque.pop(x) / deque.popleft(x)
deque는 Queue를 써야할 때 list에 비해 빠르다.
Stack의 경우 연산 시간의 차이가 많지 않다.
"""