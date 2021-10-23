# BOJ 5639 이진 검색 트리

'''


'''
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
tree = {}

def make_tree(tree, root, x):
    # 루트 노드와 비교
    if x < root:
        son = tree[root][0]
        if not son:
            tree[root][0] = x
            tree[x] = [0, 0]
        else:
            make_tree(tree, son, x)
    else:
        son = tree[root][1]
        if not son:
            tree[root][1] = x
            tree[x] = [0, 0]
        else:
            make_tree(tree, son, x)

root = 0
while True:
    n = input().rstrip()
    if n.isdigit():
        if not root:
            root = int(n)
            tree[root] = [0, 0]
        else:
            # 트리 생성함수
            make_tree(tree, root, int(n))
    else:
        break

# 후위 순회
def postorder(tree, node):
    a, b = tree[node]
    if a: postorder(tree, a)
    if b: postorder(tree, b)
    print(node, end="\n")

postorder(tree, root)