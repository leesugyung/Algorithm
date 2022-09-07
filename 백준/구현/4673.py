k=10001

a = range(1,k)
b = list()

def d(n):
    sum=n
    while True:
        r = n%10
        n = n//10
        sum+=r
        if n==0:
            break
    return sum

for i in range(1, k):
    b.append(d(i))

answer = sorted(list(set(a)-set(b)))

for i in answer:
    print(i)