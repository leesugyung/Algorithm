'''
https://aerocode.net/392
어렵당,,
'''

import sys

N = int(sys.stdin.readline())

weight = list(map(int, sys.stdin.readline().split()))

weight.sort()

check = 1
for i in weight:
    if check < i:
        break
    check += i

print(check)