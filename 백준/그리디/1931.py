'''
어렵게 빙빙 돌아간 문제
1. 시작 시간 기준으로 sort한 다음, 종료 시간 기준으로 sort한다.
-> 이렇게 되면, 빨리 종료하는 회의가 앞으로 오고 거기서 시작 시간이 빠른게 앞으로 와있어서 차례대로 포문을 돌면서 확인하기만 하면 된다.
2. for문을 돌면서 종료 시간 이후에 시작하는 미팅을 체크한다.
-> 이때 주의할 것! range(N)이 아닌 range(1, N)이 되어야 한다.
ex) 2
    1 1
    2 2
    output: 3 / answer: 2
'''

import sys

N = int(sys.stdin.readline())

meeting = []

for i in range(N):
    meeting.append(list(map(int,sys.stdin.readline().rstrip().split())))

meeting.sort(key = lambda x: x[0])
meeting.sort(key = lambda x : x[1])

count = 1
end = meeting[0][1]
for i in range(1, N):
    if end <= meeting[i][0]:
        count += 1 
        end = meeting[i][1]

print(count)