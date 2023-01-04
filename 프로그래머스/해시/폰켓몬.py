from collections import Counter

def solution(nums):
    answer = 0

    k = list(Counter(nums).keys())
    if len(k) > len(nums)/2:
        answer = len(nums)/2
    else:
        answer = len(k)

    return answer

'''
def solution(nums):
    return min(len(nums)/2, len(set(nums))
'''