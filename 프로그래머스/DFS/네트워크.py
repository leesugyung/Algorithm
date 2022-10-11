def solution(n, computers):
    answer = 0
    visited = [False]*n

    for i in range(n):
        if not visited[i]:
            DFS(n, computers, visited, i)
            answer+=1

    return answer

def DFS(n, computers,visited, index):
    visited[index]=True
    for i in range(n):
        if i != index:
            if computers[index][i] == 1 and not visited[i]:
                DFS(n, computers, visited, i)
    
