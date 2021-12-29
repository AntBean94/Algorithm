# BOJ 14725 개미굴

'''
1. Trie 자료구조 활용
2. dfs 알고리즘으로 구조 출력
'''

import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        curr_node = self.head
        # 단어로 분할
        for word in string.split():
            # 단어 비교(단어가 존재하지 않는 경우)
            if word not in curr_node.children:
                curr_node.children[word] = Node(word)
            # 현재 노드위치 변경
            curr_node = curr_node.children[word]
        # 최종 위치까지 이동한 경우 data에 삽입
        curr_node.data = string

    def structure(self):
        curr_node = self.head

        def dfs(obj, level):
            for key in sorted(obj.children.keys()):
                print(level + key)
                dfs(obj.children[key], level + "--")
        
        dfs(curr_node, "")

# main 알고리즘 시작
N = int(input())
trie = Trie()
for i in range(N):
    # 개미굴 구조 입력
    string = input().rstrip()
    # 트리 구조에 삽입
    trie.insert(string[2:])
# 개미굴 구조 출력
trie.structure()