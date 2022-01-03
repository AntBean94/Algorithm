# BOJ 5670 휴대폰 자판

'''
다음 글자가 하나뿐이라면 자동으로 입력
반드시 첫 글자는 사용자가 버튼을 눌러 입력
단어 길이의 총합은 1,000,000

시간복잡도
트라이를 만드는데: O(1,000,000)
모든 단어 탐색: O(1,000,000)
'''

import sys
input = sys.stdin.readline

# 트라이 자료구조 정의
class Node(object):
    def __init__(self, head, data=None):
        self.head = head
        self.data = data
        self.children = {}
        self.child_nums = 0

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        # 현재 위치 => 루트 노드
        curr_node = self.head

        # 삽입하기 위한 절차
        for char in string:
            # 문자가 자식에 없으면
            if char not in curr_node.children:
                # 자식 집합에 노드 생성
                curr_node.children[char] = Node(char)
                curr_node.child_nums += 1
            # 위치 이동
            curr_node = curr_node.children[char]
        # 데이터 삽입
        curr_node.data = string
    
    def search(self, string):
        curr_node = self.head
        cnt = 1
        # 탐색
        for idx, char in enumerate(string):
            if char in curr_node.children:
                # 자식이 하나 이상이면 버튼을 눌러야하므로 카운트
                if (curr_node.child_nums > 1 or curr_node.data) and idx:
                    cnt += 1
                curr_node = curr_node.children[char]
        # 탐색 종료 후 카운트 반환
        return cnt

def main():
    N = int(input())
    trie = Trie()
    # 입력
    words = [input().rstrip() for _ in range(N)]
    for i in range(N):
        trie.insert(words[i])
    total_cnt = 0
    for i in range(N):
        total_cnt += trie.search(words[i])
    # 소숫점 둘째 자리까지 반올림
    print(format(total_cnt / N + 0.000000000001, ".2f"))

while True:
    try:
        main()
    except:
        break