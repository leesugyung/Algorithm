'''
import sys

n = int(sys.stdin.readline())
A, B, C, D = [], [], [], []
AB = {}

for i in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

for i in range(n):
    for j in range(n):
        if A[i]+B[j] in AB:
            AB[A[i]+B[j]] += 1
        else:
            AB[A[i]+B[j]] = 1

count = 0
for i in range(n):
    for j in range(n):
        if -(C[i]+D[j]) in AB:
            count += AB[-(C[i]+D[j])]

print(count)
'''

