'''
문제 잘못 읽음 ;;
'''

import sys

N, S = map(int , sys.stdin.readline().split())
A = list(map(int , sys.stdin.readline().split()))

s, e = 0, 0
temp = A[e]
temp_count = 1
count = 100001

while e >= s:
    if temp_count >= count:
        temp_count -= 1
        temp -= A[s]
        s+=1
    if temp >= S:
        count = temp_count
        temp -= A[s]
        s += 1
        temp_count -= 1
        continue
    else: 
        e+=1
        temp_count += 1
    if e >= N or e < s:
        break
    temp+=A[e]

if count == 100001:
    print(0)
else:
    print(count)        