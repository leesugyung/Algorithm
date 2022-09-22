'''
몇 시간을 고민하고 실패해버림 ^__^
다음에 다시 한 번 풀어보면 좋을 것 같음.
이 문제는 한번 거친 숫자를 또 하지 않도록 하는게 제일 중요했던 문제!
괜히 계산하는 범위를 좁히겠다고 고민했는데 그럴 필요가 전혀 없었음.
'''

import sys
from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x - 1, x + 1, x*2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)

MAX = 10**5
dist = [0]*(MAX+1)

n, k = map(int, sys.stdin.readline().rstrip().split())
bfs()