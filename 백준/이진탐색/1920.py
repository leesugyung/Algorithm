'''
<in 연산자의 시간복잡도>
list, tuple

Average : O(n)
하나하나 순회하기 때문에 O(n)만큼의 시간복잡도를 갖는다
set, dictionary

Average : O(1), Worst : O(n)
내부적으로 hash를 통해 저장하므로 접근하는 시간은 O(1)이다. 하지만 해쉬의 충돌이 많아 성능이 떨어지는 경우 O(n)이 걸릴 수도 있다.

'''

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

A.sort()
for i in range(M):
    start, end = 0, N-1
    while True:
        if start > end:
            print("0")
            break
        temp = start + (end-start)//2
        if num[i] < A[temp]:
            end = temp-1
        elif num[i] > A[temp]:
            start= temp+1
        else:
            print("1")
            break