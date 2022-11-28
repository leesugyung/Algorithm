'''
LIS문제 

어림없이 내가 스스로 못푼 문제,,

일단은 1 ≤ N ≤ 1,000,000이므로
이중포문은 절대x <- 가장 긴 증가하는 부분 수열 1에서는 이중 포문으로 DP로 풀었지만
여기서는 안된다!

적어도 포문 하나로 푸는 방법을 써야하는데...

구해야하는 것 = 가장 긴 증가하는 부분 수열의 길이!

핵심 알고리즘: 정답 수열의 마지막 수보다 큰 수가 들어오면 append하고, 아니라면 그 전의 수들과 비교하여 적절한 교체 위치를 찾는 것이다.

<내가 틀린 이유>
start,end 값, 즉, 문제에서의 범위를 정확하게 설정해줘야 한다!!

문제에 따라 다르지만, 특정 문제에서는 범위를 정확하게 설정하지 않을 경우
내가 생각한 값과 도출한 답이 다를 수 있으니 정확한 범위를 설정하자.

-> 실제로 몇번 시뮬레이션을 돌려보니 실패하는 것을 볼 수 있었음

<----------------- 이진탐색의 로직 파악 ---------------->
조건문을 빠져나올 때, start= end+1 이다.(start는 항상 end보다 1만큼 크다.)
start=end 일 때 if, else 어느 조건에 들어가는지에 관계없이 start=end+1이 된다.

이분탐색의 핵심은 정답이 없는 절반을 배제하는 것 이며,
배제할 구간에 정답이 없다는 것을 확신할 수 있어야 한다.

중간값과의 비교를 통해 답의 위치를 알 수 있어야 하며
수학적으로 풀어보면, 단조성을 갖는 함수나 배열에만, 이분탐색을 적용할 수 있다.

https://www.acmicpc.net/blog/view/109
1. [start, end]가 check(start)!=check(end)가 되도록 구간으 설정
2. while(start + 1 < end) 동안 mid = (start+end)//2에서 
check(mid) = check(start)라면, start = mid
아니라면, end = mid
3. 구한 경계에서 답이 start인지 end인지 생각해보고 출력



'''
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
D = [0]

for i in range(N):
    if D[-1] < A[i]:
        D.append(A[i])
    elif D[-1] > A[i]:
        start = 0
        end = len(D)-1
        while start<=end:
            mid = (start+end)//2
            if D[mid]>=A[i]:
                end = mid-1
            else:
                start = mid+1
        D[start]=A[i]

print(len(D)-1)