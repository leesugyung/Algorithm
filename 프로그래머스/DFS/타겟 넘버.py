import sys

def solution(numbers, target):
    answer = 0

    def DFS(index, sum):
        if index == len(numbers):
            if sum == target:
                nonlocal answer
                answer += 1
            return
        else:
            DFS(index+1, sum + numbers[index])
            DFS(index+1, sum - numbers[index])
    
    DFS(0, 0)

    return answer
    

answer = solution([1, 1, 1, 1, 1], 3)

print(answer)