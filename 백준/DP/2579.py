import sys

N = int(sys.stdin.readline())

score = [0]*301

for i in range(N):
    score[i]=(int(sys.stdin.readline()))

d = [0]*301
d[0] = score[0]
d[1] = score[0] + score[1]
d[2] = max(score[2]+score[1], score[2]+score[0])

for i in range(3, N):
    d[i] = max(d[i-2]+score[i], score[i]+score[i-1]+d[i-3])
print(d[N-1])