import sys

S = list(sys.stdin.readline().rstrip())

end = 0

while S:
    if S[0] == '<':
        end = S.index('>')
        print(''.join(S[0:end+1]), end='')
        del S[0:end+1]
        end = 0
    else:
        if '<' in S and ' ' in S:
            end1 = S.index('<')
            end2 = S.index(' ')
            if end1 < end2:
                end = end1
                string = S[0:end]
                string.reverse()
                print(''.join(string), end='')
                del S[0:end]
                end = 0
            else :
                end = end2
                string = S[0:end]
                string.reverse()
                print(''.join(string), end=' ')
                del S[0:end+1]
                end = 0
        elif '<' in S:
            end = S.index('<')
            string = S[0:end]
            string.reverse()
            print(''.join(string), end='')
            del S[0:end]
            end = 0
        elif ' ' in S:
            end = S.index(' ')
            string = S[0:end]
            string.reverse()
            print(''.join(string), end=' ')
            del S[0:end+1]
            end = 0
        else:
            S.reverse()
            print(''.join(S), end='')
            S.clear()