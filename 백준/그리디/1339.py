'''
구현을 어떻게 해야될 지 감도 안 잡힌^^문제 -> 나중에 한 번 다시 풀어보장

딕셔너리를 사용해야 했음. 딕셔너리를 이때까지 한 번도 안써봄:(
    1. 알파벳을 딕셔너리에 저장한다. 이때, 단어의 길이에 따라 알파벳의 자리수가 정해지므로 자릿수를 체크하여 그 자리에 맞는 값을 매칭시킨다.
    2. 매칭을 완료한 후에, dict의 value만 가져와 리시트에 내림차순으로 정렬한다. -> 가장 큰 비율을 차지하는 것부터 앞에 등장함.
    3. 이 리스트의 첫 수부터 차례대로 9,8,7, ...를 곱한다.

'''
import sys

N = int(sys.stdin.readline())

words = []
dic = {}
sum = 0
check = 9

for i in range(N):
    words.append(sys.stdin.readline().strip())

for i in range(N):
    for j in range(len(words[i])):
        if words[i][j] in dic:
            dic[words[i][j]] += 10**(len(words[i])-j-1)
        else:
            dic[words[i][j]] = 10**(len(words[i])-j-1)

value = list(dic.values())

value.sort(reverse=True)

for i in value:
    sum += i*check
    check -= 1

print(sum)