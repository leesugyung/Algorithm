import sys
import heapq

N = int(sys.stdin.readline())

h = []
meeting = []

for i in range(N):
    meeting.append(list(map(int, sys.stdin.readline().rstrip().split())))

meeting.sort()

heapq.heappush(h, meeting[0][1])
for i in range(1, N):
    if h[0] > meeting[i][0]:
        heapq.heappush(h, meeting[i][1])
    else:
        heapq.heappop(h)
        heapq.heappush(h, meeting[i][1])

print(len(h))