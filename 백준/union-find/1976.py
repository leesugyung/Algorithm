import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

parent = [0]
for i in range(1, n+1):
    parent.append(i)
level = [1]*(n+1)

def find(x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_p = find(x)
    y_p = find(y)

    if x_p == y_p:
        return

    if level[x_p] > level[y_p]:
        parent[y_p] = x_p
    else:
        parent[x_p] = y_p
    if level[x_p] == level[y_p]:
        level[y_p] += 1

for i in range(1, n+1):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(len(temp)):
        if temp[j] == 1:
            union(i, j+1)
            
plan = list(map(int, sys.stdin.readline().split()))

result = True

for i in range(len(plan)-1):
    if find(plan[i]) != find(plan[i+1]):
        result = False
        break

if result:
    print("YES")
else:
    print("NO")