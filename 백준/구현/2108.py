import sys
from collections import Counter

N = int(sys.stdin.readline())
nums = []
sum = 0

for i in range(N):
    num = int(sys.stdin.readline())
    nums.append(num)
    sum += num
nums.sort()

#산술평균
#반올림하는 함수 round()
print(round(sum/N))

#중앙값
print(nums[N//2])

#최빈값
freq = Counter(nums).most_common()
if len(freq)>1:
    if freq[0][1]==freq[1][1]:
        print(freq[1][0])
    else:
        print(freq[0][0])
else:
    print(freq[0][0])

#범위
print(nums[N-1]-nums[0])

'''
Counter 라이브러리 
from collections import Counter
: 각 원소가 몇 번씩 나오는지가 저장된 객체를 반환

ex)
>>> Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
Counter({'hi': 3, 'hey': 2, 'hello': 1})

>>> Counter("hello world")
Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

가장 흔한 데이터 찾기
Counter 클래스의 most_common() 메서드
: 데이터의 개수가 많은 순으로 정렬된 배열을 리턴

ex)
Counter('hello world').most_common()
[('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]

Counter('hello world').most_common(1) #1개만 반환
[('l', 3)]
'''