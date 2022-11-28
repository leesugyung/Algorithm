'''
파라메트릭 서치 -> 단독 문제로 나오기보다는 다른 알고리즘과 결합해서 출제됨.
"최적화문제(문제의 상황을 만족하는 특정 변수의 최솟값, 최댓값을 구하는 문제)를 결정문제로 바꾸어 푸는 것

파라메트릭 서치는 문제를 풀어나가는 과정이 바이너리 서치(이분 탐색)와 매우 흡사
파라메트릭 서치를 쓰려면?
1. 해당값이 정답인지 아닌지를 쉽게 판단할 수 있어야 함(즉, 결정문제를 쉽게 풀 수 있다.)
2. 정답이 될 수 있는 값들이 연속적이어야 한다.

이건 왜 파라메트릭 서치/ 이진 탐색일까?
일단 for문으로 xi를 보는건 완전 안된다 -> 시간초과가 100% 발생 => 다르게 서치해야겠네? logN
일단 이 문제는 최적화 문제인데, 연속적인 값들이며(거리) 해당 값이 정답인지 아닌지 쉽게 판단가능하다

내가 잘못 생각한 부분!
문제에서 구해야 하는건 point가 아니라 거리!
따라서 start, end 이것도 point가 아니라 거리로 설정했어야 했다
start = 최소거리, end = home[-1]-home[0]
mid가 따라서 정답이 되는데
mid를 바꿔가면서 답을 구해가는 것임!

+ current = i를 해줘야되는데
이유는 mid이 가장 인접한 두 공유기 사이 거리인데
만약? 저걸 안해주면 mid보다 더 인접한 거리인 home들도 count해버림 ㄷㄷ

'''

import sys

N, C = map(int, sys.stdin.readline().split())
home = []
for i in range(N):
    home.append(int(sys.stdin.readline()))

home.sort()
start, end = 1, home[-1]-home[0]

while start<=end:
    mid = (start+end)//2
    current = home[0]
    count = 1
    for i in home:
        if i >= current+mid:
            count+=1
            current = i
    if count < C:
        end=mid-1
    else:
        start=mid+1
        answer = mid

print(answer)  