import sys

N = int(sys.stdin.readline())


RGB = []
for i in range(N):
    RGB.append(list(map(int, sys.stdin.readline().strip().split())))

'''
내가 푼 코드

d = [[1000001]*3 for _ in range(N)]
d[0] = RGB[0]

for i in range(1, N):
    for j in range(3):
        for r in range(3):
            if j != r:
                d[i][j] = min(d[i][j], RGB[i][j]+d[i-1][r])

result = min(d[N-1])
print(result)
'''

for i in range(1, N):
    RGB[i][0] += min(RGB[i-1][1], RGB[i-1][2])
    RGB[i][1] += min(RGB[i-1][0], RGB[i-1][2])
    RGB[i][2] += min(RGB[i-1][0], RGB[i-1][1])

print(min(RGB[N-1]))