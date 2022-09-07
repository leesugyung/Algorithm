K = int(input())
sum = 0
list = []

for i in range(0, K):
    num = int(input())
    if num == 0:
      del list[len(list)-1]
      continue
    list.append(num)  

for i in range(0, len(list)):
    sum += int(list[i])

print(sum)