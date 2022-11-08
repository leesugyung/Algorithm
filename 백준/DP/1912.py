import sys

N = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    num[i] = max(num[i]+num[i-1],num[i])

print(max(num))