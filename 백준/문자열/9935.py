'''
list에서 del, remove, pop의 차이
remove는 특정 색인이 아닌 첫 번째 일치 값을 제거
del은 특정 인덱스에서 항목을 제거
pop은 특정 인데스에서 항목을 제거하고 반환
-> del이 pop보다 수행속도 빠르다
+ del은 pop과 다르게 리스트의 범위를 지정해 삭제할 수 있다.
'''
import sys

s = list(sys.stdin.readline().rstrip())
bomb = list(sys.stdin.readline().rstrip())

last = bomb[-1]
l = len(bomb)
stack = []

for char in s:
    stack.append(char)
    if char == last and stack[-l:] == bomb:
        del stack[-l:]

if stack:
    print(''.join(stack))
else:
    print("FRULA")