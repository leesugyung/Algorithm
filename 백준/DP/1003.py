import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    one, zero = 0, 0
    
    dzero = [0]*(N+1)
    done = [0]*(N+1)
    dzero[0] = 1
    if N != 0:
        done[1] = 1

    for i in range(2, N+1):
        dzero[i] = dzero[i-2] + dzero[i-1]
        done[i] = done[i-2] + done[i-1]

    print(dzero[N], end = " ")
    print(done[N])