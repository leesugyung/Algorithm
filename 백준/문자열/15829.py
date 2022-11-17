import sys

L = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()
r, M = 31, 1234567891

sum = 0
for i in range(L):
    sum += (ord(S[i])-ord('a')+1)*(r**i)

print(sum%M)