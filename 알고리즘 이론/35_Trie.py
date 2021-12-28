# 35 Trie 자료구조

'''
시간 복잡도(문자열 L, 문자열의 수 M)
1. 트라이의 생성: O(ML)
2. 탐색: O(L)
'''

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    # 문자열 삽입
    def insert(self, string):
        curr_node = self.head

        # 삽입할 String 각각의 문자에 대해 자식 Node를 만들며 내려간다.
        for char in string:
            # 자식 Node들 중 같은 문자가 없으면 Node를 새로 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            
            # 같은 문자가 있으면 노드를 생성하지 않고 해당 노드로 이동
            curr_node = curr_node.children[char]
        
        # 문자열이 끝난 지점의 노드의 data값에 해당 문자열을 표시
        curr_node.data = string

    # 문자열이 존재하는지 탐색
    def search(self, string):
        # 가장 아래에 있는 노드에서부터 탐색을 시작한다.
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        
        # 탐색이 끝난 후에 해당 노드의 data값이 존재한다면
        # 문자가 포함되어 있다는 의미.
        if curr_node.data is not None:
            return True