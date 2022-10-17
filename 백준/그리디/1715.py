'''
예외케이스 -> 카드뭉치가 1개일 경우 비교회수가 0이다.

PriorityQueue (VS) heapq
속도 차이가 있다. heap가 빠르다.

why? queue 속 PriorityQueue 는 Thread-Safe 하고 heapq는 Non-safe 하기 때문이라고 한다.
Thread Safe 하다는 것은 반드시 확인 절차를 걸쳐야 하기 때문에 확인하는 작업떄문에 더 느리다.
'''

'''
import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())

q = PriorityQueue()

for i in range(N):
    q.put(int(sys.stdin.readline()))

sum = 0

while True:
    if q.qsize() == 1:
        sum = 0
        break
    x = q.get()
    y = q.get()
    sum += x+y
    if q.empty():
        break
    q.put(x+y)

print(sum)
'''

import heapq
import sys

N = int(sys.stdin.readline())
heap = []
sum = 0

for i in range(N):
    heapq.heappush(heap, int(sys.stdin.readline()))

while True:
    if len(heap)==1:
        sum = 0
        break
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    sum += x+y
    if not len(heap):
        break
    heapq.heappush(heap, x+y)

print(sum)