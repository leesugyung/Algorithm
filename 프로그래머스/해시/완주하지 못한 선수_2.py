from collections import Counter

participant	= ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

'''
print(list(Counter(participant).keys()))
result = list(Counter(participant) - Counter(completion))[0]

print(result)
'''

dir = {}
temp = 0

for i in participant:
    dir[hash(i)] = i
    print(hash(i), int(hash(i)), type(hash(i)), type(int(hash(i))))
    temp += hash(i)
for i in completion:
    temp -= hash(i)
result = dir[temp]

print(result)