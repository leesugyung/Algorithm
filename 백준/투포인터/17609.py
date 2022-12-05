'''
axaaxaa -> 이런 경우를 생각하지 못함.
'''
'''
import sys

T = int(sys.stdin.readline())

for i in range(T):
    string = sys.stdin.readline().rstrip()
    
    start , end = 0, len(string)-1
    check = 0
    temp = []
    while start <= end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            if check == 1 or end-start==1:
                if temp:
                    start, end = temp.pop()
                    continue
                check = 2
                break
            if string[start+1] == string[end] and string[start] == string[end-1]:
                check = 1
                temp.append([start+2, end-1])
                temp.append([start+1, end-2])
                start, end = temp.pop()

            elif string[start] == string[end-1]:
                start += 1
                end -= 2
                check = 1
            elif string[start+1] == string[end]:
                start += 2
                end -= 1
                check = 1
            else:
                if temp:
                    start, end = temp.pop()
                    continue
                check = 2 
                break
    print(check)
'''
'''
#정식 풀이

import sys

def is_palindrome(start, end):
    check = 1
    while start<=end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            check = 0
            return check
    return check

def is_pseudo_palindrome(start, end):
    check = 0
    temp1, temp2 = 0, 0
    while start <= end:
        if string[start]==string[end]:
            start += 1
            end -= 1
        else:
            if string[start+1] == string[end]:
                temp1 = is_palindrome(start+1, end)
            if string[start] == string[end-1]:
                temp2 = is_palindrome(start, end-1)
            if temp1 or temp2:
                check = 1
                break
            else:
                check = 2
                break
    return check


n = int(sys.stdin.readline())

for i in range(n):
    string = sys.stdin.readline().rstrip()
    start, end = 0, len(string)-1
    print(is_pseudo_palindrome(start, end))

'''
import sys

def ispseudo(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def ispalindrome(word, left, right):
    if word == word[::-1]:
        return 0
    else:
        while left < right:
            if word[left] != word[right]:
                check_left = ispseudo(word, left + 1, right)
                check_right = ispseudo(word, left, right - 1)

                if check_left or check_right:
                    return 1
                else:
                    return 2
            else:
                left += 1
                right -= 1

T = int(sys.stdin.readline().rstrip("\n"))

for _ in range(T):
    word = sys.stdin.readline().rstrip("\n")
    left, right = 0, len(word)-1
    answer = ispalindrome(word, left, right)
    print(answer)