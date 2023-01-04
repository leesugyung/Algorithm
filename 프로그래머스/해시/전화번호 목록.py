def solution(phone_book):
    answer = True
    l = set()
    target = set()
    check = set() 
    num = len(phone_book)

    for i in phone_book:
        l.add(len(i))

    for i in l:
        check = set()
        target = set()
        count = 0
        for j in phone_book:
            if len(j)>i:
                target.add(j[:i])
            elif len(j)==i:
                check.add(j)
        if len(target) != len(target-check):
            answer = False

    return answer