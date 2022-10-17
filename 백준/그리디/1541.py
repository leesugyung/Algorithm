"""
쉬운 문제 but 나는 복잡하게 푼 느낌
"""

"""
import sys

expression = list(sys.stdin.readline().rstrip().split('-'))

sum = 0
for i in range(len(expression)):
    if i == 0:
        if expression[0] == '': #조건 좀 제대로 읽자! (처음과 마지막 문자는 숫자이다.)
            continue
        if '+' in expression[0]:
            temp = list(map(int, expression[0].split('+')))
            for j in temp:
                sum += j
        else:
            sum = int(expression[0])

    else:
        temp_sum = 0
        if '+' in expression[i]:
            temp = list(map(int, expression[i].split('+')))
            for j in temp:
                temp_sum += j
            sum -= temp_sum
        else:
            sum -= int(expression[i])

print(sum)
"""

import sys

expression = sys.stdin.readline().rstrip().split('-')
check = []

for i in expression:
    temp_sum = 0
    temp = i.split('+')
    for j in temp:
        temp_sum += int(j)
    check.append(temp_sum)

sum = int(check[0])

for i in range(1, len(check)):
    sum -= check[i]

print(sum)