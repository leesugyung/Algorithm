'''
import sys

N = int(sys.stdin.readline())
count = 0

while N:
    if 2<N<15:
        if not N%3:
            count+=int(N//3)
            break
        else:
            N=N-5
            count+=1
    elif N<=2:
        print(-1)
        exit(0)
    else:
        N=N-5
        count+=1 

print(count)
'''

import sys

N = int(sys.stdin.readline())
count = 0

while N:
    if N<3:
        print(-1)
        exit(0)

    if not N%5:
        count+=N//5
        break
        
    N -= 3
    count += 1

print(count)