'''
Union-Find는 대표적인 그래프 알고리즘 = 합집합 찾기
서로소 집합(Disjoint-set) 알고리즘이라고도 부른다.
-> 여러 개의 노드가 존재할 때 두 개의 노드를 선택해서, 현재 이 두 노드가 서로 같은 그래프에 속하는지 판별하는 알고리즘이다.

Disjoint-set: 서로 공통된 원소를 가지고 있지 않은 두 개 이상의 집합

Union-Find의 시간 복잡도
평균적으로 트리의 높이만큼 탐색하는 O(logN)이지만, 트리를 형성하는 과정에서 사향트리(Skewed Tree)가 될 수 있으며 이렇게 될 경우 시간 복잡도는 O(N)이 되어버림.

따라서, 효율성을 위해 Find 과정에서 경로 압축을 할 수 있다.
Find 함수를 호출할 때마다 트리의 높이가 달라져 수행시간이 변한다.

경로 압축을 하는 find의 시간복잡도는 O(a(N))인데 이때, a(N)은 아커만 함수이다.
아커만 함수는 상수의 시간 복잡도를 가진다고 봐도 무방하다.
'''
import sys

n, m = map(int, sys.stdin.readline().split())

parent = []
for i in range(n+1):
    parent.append(i)
level = [1]*(n+1)

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a_parent = find(a)
    b_parent = find(b)

    if level[a_parent]>level[b_parent]:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent
    if level[a_parent]==level[b_parent]:
        level[b_parent] += 1

for i in range(m):
    cal, a, b = map(int, sys.stdin.readline().split())
    if cal == 0:
        union(a, b)

    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")