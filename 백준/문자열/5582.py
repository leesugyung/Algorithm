import sys

def solve():
    s1 = sys.stdin.readline().rstrip()
    s2 = sys.stdin.readline().rstrip()

    d = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    result = 0

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                d[i][j] = d[i-1][j-1]+1
                result = max(result, d[i][j])
    print(result)

if __name__ == '__main__':
    solve()