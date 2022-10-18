'''
보석 N개 -> 보석의 무게 M, 가격 V
가방 K개 -> 가방의 최대 무게 C
가방에는 최대 한 개의 보석만 넣을 수 있음
=> 보석의 최대 가격?

당차게 시간초과^^ -> 아니 최소힙, 최대힙을 둘 다 사용해야되는건 어케아냐
                    포문을 돌면 N인데 힙으로 돌면 logN이라서 그런가?

'''
import sys
import heapq

N, K = map(int, sys.stdin.readline().rstrip().split())

h = []
for i in range(N):
    heapq.heappush(h, list(map(int, sys.stdin.readline().rstrip().split())))

C = []
for i in range(K):
    C.append(int(sys.stdin.readline().rstrip()))

C.sort()

count = 0
sum = 0

temp_h = []
for bag in C:
    while h and bag >= h[0][0]:
        heapq.heappush(temp_h, -heapq.heappop(h)[1])
    if temp_h:
        sum -= heapq.heappop(temp_h)
    elif not h:
        break

print(sum)