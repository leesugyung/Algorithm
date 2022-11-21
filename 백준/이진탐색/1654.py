import sys

K, N = map(int, sys.stdin.readline().split())
line = []

for i in range(K):
    line.append(int(sys.stdin.readline()))

end = max(line)
start = 1

while start <= end:
    mid = (start+end)//2

    count = 0
    for i in line:
        count += i//mid
    if count >= N:
        start = mid+1
    else:
        end = mid-1

print(end)