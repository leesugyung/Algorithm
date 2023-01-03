def solution(participant, completion):
    answer = ''
    d = {}

    for i in completion:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    for i in participant:
        if (i in d) and (d[i]>0):
            d[i] -= 1
        else:
            answer = i
            print(i)
            break

    return answer