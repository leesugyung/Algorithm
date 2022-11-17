'''
시간 초과를 피하려면
파이썬에서 arr [a:b]의 시간 복잡도는 O(b - a)
슬라이스를 최대한 덜 쓰고 반복을 최소화하는 방법을 찾아야 한다.
'''
import sys

def solve():
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    S = sys.stdin.readline().rstrip()

    result = 0
    index = 0
    temp = 0
    while index < M:
        if S[index:index + 3] == "IOI":
            index += 2
            temp += 1
            if temp == N:
                result+=1
                temp -= 1
        else:
            index += 1
            temp = 0

    return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solve())