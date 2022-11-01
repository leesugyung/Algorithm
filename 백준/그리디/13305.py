import sys

N = int(sys.stdin.readline())

road = list(map(int, sys.stdin.readline().rstrip().split()))
price = list(map(int, sys.stdin.readline().rstrip().split()))

min = price[0]
sum = 0

for i in range(0, N-1):
    if min > price[i]:
        min = price[i]
        
    sum += road[i]*min

print(sum)