'''
이분탐색을 써야된다는 생각은 미처 못했음..
'''
'''
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

A.sort()
m = sys.maxsize

for i in range(N-1):
    start = i+1
    end = N-1
    while start <= end:
        mid = (start+end)//2
        temp = A[i] + A[mid]
        if abs(temp) < abs(m):
            m = temp
            result = [A[i], A[mid]]
        if temp < 0:
            start = mid+1
        else:
            end = mid-1

result.sort()
print(' '.join(list(map(str, result))))
'''
# 훨씬 적게 걸리는 정석 풀이 ㄷㄷ

import sys

# input 입력 받기
n = int(sys.stdin.readline())
solution = list(map(int, sys.stdin.readline().split()))

# 정렬하기
solution.sort()

# 이중포인터 설정
left = 0
right = n-1

answer = 2e+9+1 # 기준값
final = [] # 정답

# 투포인터 진행
while left < right:
    s_left = solution[left]
    s_right = solution[right]

    tot = s_left + s_right
    # 두 용액의 합이 0과 가장 가까운 용액을 정답에 담아주기
    if abs(tot) < answer:
        answer = abs(tot)
        final = [s_left, s_right]
	
    # 두 용액의합이 0보다 작다면 왼쪽의 값을 늘려 조금 더 0에 가깝게 만들어준다
    if tot < 0:
        left += 1
    # 반대로, 두 용액의 합이 0보다 크다면 오른쪽의 값을 줄여서 조금 더 0에 가깝게 만들어준다
    else:
        right -= 1

print(final[0], final[1])