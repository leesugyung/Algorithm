'''
10진수 -> 2진수
1. 나누어지지 않을 때까지 나누어준다.
2. 마지막 나머지부터 처음 나머지까지 차례대로 써준다.
=> 8진수, 16진수도 동일하다.

2진수 -> 8진수
1. 8 = 2^3이므로 뒤에서부터 3자리씩 끊어준다.
(세 자리씩 안나누어지면 0으로 채워준다.)
2. 나눈 세 자리씩 8진수로 변환
3. 앞자리부터 차례대로 써주기

8진수 -> 2진수
1. 한 자리씩 끊어준다.
2. 각각의 수를 3자리 수의 2진수로 변환한다.
3. 차례대로 붙여준다.

2진수 -> 16진수
1. 16 = 2^4이므로 뒤에서부터 4자리씩 끊어준다.
2. 각각을 10진수로 변환한다.
3. 10진수로 표현된 각 숫자에 대응되는 16진수로 변환한다.
'''

'''
import sys
from collections import deque

Octal = list(sys.stdin.readline().rstrip())
Binary = deque()

for i in range(len(Octal)-1, -1, -1):
    temp = int(Octal[i])
    for j in range(3):
        Binary.appendleft(str(temp%2))
        temp //= 2
        if i == 0 and temp == 0:
            break

print(''.join(Binary))
'''
import sys

print(bin(int(sys.stdin.readline().strip(), 8))[2:])