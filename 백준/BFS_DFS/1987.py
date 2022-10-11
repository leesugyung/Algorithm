'''
시간초과로 고생한 문제
-> 포문을 최대한 없애야 했음 + index나 deque(x) set(o)

list vs set
list: 순서가 존재, indexing 존재, 변경가능
set: 순서x, 중복 불가, 키 값으로만 존재
-> 리스트보다 집합에서 원소의 포함 여부를 빠르게 계산할 수 있다.
'''
import sys

def DFS(r, c, cnt):
    dx = [-1, 1, 0, 0]
    dy = [0, 0 , -1, 1]
    global max_cnt

    for i in range(4):
        x = r + dx[i]
        y = c + dy[i]

        if x < 0 or x > R-1 or y < 0 or y > C-1:
            continue

        if G[x][y] not in alphabet:
            alphabet.add(G[x][y])
            DFS(x, y, cnt+1)
            alphabet.remove(G[x][y])
    if max_cnt < cnt:
        max_cnt = cnt

R, C = map(int, sys.stdin.readline().rstrip().split())
G = []

for _ in range(R):
    G.append(list(sys.stdin.readline().rstrip()))

max_cnt = 0
alphabet = set()
alphabet.add(G[0][0])
DFS(0, 0, 1)

print(max_cnt)