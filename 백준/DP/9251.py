'''
LCS(Longest Common Subsequence)?
공통 부분 문자열 중 가장 길이가 긴 문자열

<Substring vs Subsequence>
Substring: 전체 문자열에서 연속된 부분 문자열
Subsequence: 전체 문자열에서 꼭 연속된 문자열인 것은 아닌 부분 문자열

너무 어렵다,,
i랑 j를 가지고 장난치는 기분
좀 짜증난다 이걸 어떻게 알지?ㅜㅜ
'''
import sys

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()

d = [[0]*(len(s2)+1) for _ in range(len(s1)+1) ]

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i-1][j], d[i][j-1])

print(d[len(s1)][len(s2)])