import sys

T = int(sys.stdin.readline())

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, level, x, y):
    p_x = find(parent, x)
    p_y = find(parent, y)

    if p_x == p_y:
        return

    if level[p_x]>level[p_y]:
        parent[p_y] = p_x
        count[p_x] += count[p_y]
    else:
        parent[p_x] = p_y
        count[p_y] += count[p_x]
    if level[p_x]==level[p_y]:
        level[p_y] += 1

for i in range(T):
    F = int(sys.stdin.readline())

    parent = []
    for k in range(F*2):
        parent.append(k)

    level = [1]*(F*2)
    count = [1]*(F*2)
    d = {}
    check = 0

    for j in range(F):
        a, b = sys.stdin.readline().split()
        if not a in d:
            d[a] = check
            check += 1
        if not b in d:
            d[b] = check
            check += 1
        x, y = d[a], d[b]
        union(parent, level, x, y)
        p_x = find(parent, x)
        print(count[p_x])