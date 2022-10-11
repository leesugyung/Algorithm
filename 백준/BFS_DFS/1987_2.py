'''
1. 알파벳을 아스키코드를 이용해 숫자로 변환한다.
2. 26개의 0을 담고있는 visited 리스트를 만들어준다.
3. 각각의 알파벳을 방문했을 때 그 알파벳에 해당하는 인덱스를 1로 바꾸어 방문 처리를 한다.

ord() 함수 : 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환한다.

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

        if not visited[G[x][y]]:
            visited[G[x][y]] = True
            DFS(x, y, cnt+1)
            visited[G[x][y]] = False
    if max_cnt < cnt:
        max_cnt = cnt
    

R, C = map(int, sys.stdin.readline().rstrip().split())
G = []

for _ in range(R):
    G.append(list(map(lambda a : ord(a)-ord('A'), sys.stdin.readline().rstrip())))

max_cnt = 0
visited = [False]*26
visited[G[0][0]] = True
DFS(0, 0, 1)

print(max_cnt)