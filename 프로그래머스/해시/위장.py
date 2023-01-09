def solution(clothes):
    answer = 1
    d = {}
    
    for name, kind in clothes:
        if kind in d:
            d[kind] += 1
        else:
            d[kind] = 1
    
    for i in list(d.values()):
        answer *= (i+1)
    answer -= 1
    
    return answer