def solution(genres, plays):
    answer = []
    d = {}
    
    for i in range(len(plays)):
        if genres[i] in d:
            d[genres[i]][0] += plays[i]
            d[genres[i]][1].append([i, plays[i]])
        else:
            d[genres[i]] = [plays[i]]
            d[genres[i]].append([[i, plays[i]]])
            
    l = list(d.values())
    l.sort(key = lambda x: x[0], reverse = True)
    
    for temp in l:
        if len(temp[1]) == 1:
            answer.append(temp[1][0][0])
        else:
            temp[1].sort(key = lambda x: x[1], reverse = True)
            answer.append(temp[1][0][0])
            answer.append(temp[1][1][0])
        
    return answer