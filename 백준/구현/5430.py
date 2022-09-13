import sys

T = int(sys.stdin.readline())

for i in range(0,T):
    check_D = 0
    check_R = 0
    check_E = False

    p = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline())
    arr = list(sys.stdin.readline().rstrip().split(","))

    start = 0
    back = n-1

    arr[0]=arr[0][1:]
    arr[n-1]=arr[n-1][:-1]

    for i in p:
        if i == 'R':
            check_R += 1
        elif i == 'D':
            if start > back :
                check_E = True
                break
            else :
                if check_R%2: #홀수번째
                    back -= 1
                else:
                    start +=1
    
    if check_E:
        print("error")
    else:
        output = arr[start:back+1]
        if check_R%2:
            output.reverse()
        print("["+",".join(output)+"]")

#입출력으로 고생한 문제 