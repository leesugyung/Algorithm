'''
와 이걸 어케 함,,? 진짜 멍청해지는 기분 ㅎㅎ;;
나중에 꼭 꼭 풀어보기!
'''

import sys

def DFS(r, c):
    if r == M-1 and c == N-1:       
        return 1

    if visited[r][c] == -1:
        visited[r][c] = 0
        for i in range(4):
            x = r + dx[i]
            y = c + dy[i]
            if 0 <= x < M and 0 <= y < N:
                if G[x][y] < G[r][c]:
                    visited[r][c] += DFS(x, y)
    return visited[r][c]

M, N = map(int, sys.stdin.readline().rstrip().split())

G = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(M):
    G.append(list(map(int, sys.stdin.readline().rstrip().split())))

visited = [[-1]*N for _ in range(M)]

print(DFS(0,0))