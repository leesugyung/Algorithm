'''
[DP] 0/1 knapsack(배낭) 문제
: 배낭에 담을 수 있는 무게의 최댓값이 정해져 있고, 일정 가치와 무게가 있는 짐들을 배낭에 넣을 때  
가치의 합이 최대가 되도록 짐을 고르는 방법을 찾는 문제!

MAX(현재 가치+남은 가방 크기만큼 넣을 때 최대 가치, 이전까지 구해둔 가치)

알고리즘 -> 
1) x축엔 가방 1~K까지의 무게, y축은 물건 N개 개수만큼의 배열을 만들어준다.
2) 행을 차례대로 돌며 다음과 같은 알고리즘을 수행해준다.
3-0) 현재 물건이 현재 돌고있는 무게보다 작다면, 바로 [이전물건][같은무게]를 입력해준다. (knapsack[i-1][j]를 입력해준다.)
3-1) 현재 물건을 넣어준다. 물건을 넣은 뒤의 남은 무게를 채울 수 있는 최댓값(Knapsack[i-1][j-weight])을 위의 행에서 가져와 더해준다.
3-2) 현재 물건을 넣지 않고, 다른 물건들로 채우는 값(knapsack[i-1][j])을 가져온다.
4) 3-1과 3-2 중 더 큰 값을 Knapsack[i][j]에 저장해준다. 이 값은 현재까지의 물건들로 구성할 수 있는 가장 가장 가치 높은 구성이다.
5) Knapsack[N][K]는 K무게일 때의 최댓값을 가리킨다.

'''
import sys

N, K = map(int,sys.stdin.readline().split())

item = [[0]]

for i in range(N):
    item.append(list(map(int, sys.stdin.readline().rstrip().split())))

knapsack = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = item[i][0]
        value = item[i][1]
        if weight > j:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(value+knapsack[i-1][j-weight], knapsack[i-1][j])

print(knapsack[N][K])