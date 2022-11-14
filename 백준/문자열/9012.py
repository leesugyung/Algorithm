import sys

T = int(sys.stdin.readline())

for i in range(T):
    s = sys.stdin.readline().strip()
    h = []
    check = 0
    for j in s:
        if j =="(":
            h.append(1)
        else:
            if h:
                h.pop()
            else:
                check = 1
                break
    if h or check==1:
        print("NO")
    else:
        print("YES")