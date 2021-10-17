# BOJ 1991 트리 순회

'''
1. 전위 순회(Preorder)
- 노드를 방문한다.
- 왼쪽 서브 트리를 전위 순회한다.
- 오른쪽 서브 트리를 전위 순회한다.
=> 깊이 우선 순회(depth-first traversal)라고도 한다.

2. 중위 순회(Inorder)
- 왼쪽 서브 트리를 중위 순회한다.
- 노드를 방문한다.
- 오른쪽 서브 트리를 중위 순회한다.
=> 대칭 순회(symmetric)라고도 한다.

3. 후위 순회(Postorder)
- 왼쪽 서브 트리를 후위 순회한다.
- 오른쪽 서브 트리를 후위 순회한다.
- 노드를 방문한다.

4. 레벨 순서 순회(level-order)
- 모든 노드를 낮은 레벨부터 차례대로 순회한다.
- 너비 우선 순회(breadth-first traversal)라고도 한다.
'''

N = int(input())
tree = {}
for i in range(N):
    a, b, c = map(str, input().split())
    tree[a] = [b, c]

def preorder(x):
    print(x, end="")
    if tree[x][0] != '.': preorder(tree[x][0])
    if tree[x][1] != '.': preorder(tree[x][1])

def inorder(x):
    if tree[x][0] != '.': inorder(tree[x][0])
    print(x, end="")
    if tree[x][1] != '.': inorder(tree[x][1])

def postorder(x):
    if tree[x][0] != '.': postorder(tree[x][0])
    if tree[x][1] != '.': postorder(tree[x][1])
    print(x, end="")

start = 'A'
preorder(start)
print()
inorder(start)
print()
postorder(start)