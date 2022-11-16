'''
트라이(Trie): 문자열을 저장하고 효율적으로 탐색하기 위한 트리 형태의 자료구조

'''
import sys
class Node(object):
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string
    
    def starts_with(self, prefix):
        current_node = self.head
        
        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return False
        
        if current_node.children:
            return False
        else:
            return True

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    trie = Trie()
    number = []
    for j in range(n):
        temp = sys.stdin.readline().rstrip()
        number.append(temp)
        trie.insert(temp)

    for j in range(len(number)):
        if trie.starts_with(number[j]) == False:
            print("NO")
            break
        elif j == len(number)-1:
            print("YES")