N=int(input())

count=0

def checker(check):
    a = [check[0]]
    k = check[0]

    for i in range(1, len(check)):
        if check[i]==k:
            continue
        else:
            for j in range(0, len(a)):
                if a[j]==check[i]:
                    return False
            a.append(check[i])
            k=check[i]
    
    return True

for i in range(0, N):
    check=input()
    if checker(check):
        count+=1

print(count)