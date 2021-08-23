# Segment Tree 예제

import math
import sys
input = sys.stdin.readline

# Segment Tree 
def segment_tree(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        tree[node] = segment_tree(arr, tree, node*2, start, (start+end)//2) + segment_tree(arr, tree, node*2+1, (start + end)//2+1, end)
        return tree[node]

# Find sum
def find_sum(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    elif left <= start and end <= right:
        return tree[node]
    else:
        return find_sum(tree, node*2, start, (start+end)//2, left, right) + find_sum(tree, node*2+1, (start+end)//2+1, end, left, right)

# Update
def update(tree, node, start, end, index, diff):
    if index < start or index > end: return
    tree[node] = tree[node] + diff
    if start != end:
        update(tree, node*2, start, (start+end)//2, index, diff)
        update(tree, node*2+1, (start+end)//2+1, end, index, diff)


'''
H = 트리의 높이
N = 리프노드의 갯수

case 1. 완전 이진트리: H = logN + 1

case 2. 이진트리: H = logN + 2

=> segment tree 배열의 크기: 2^H - 1
'''
arr = list(map(int, input().split()))
N = arr[0]
H = math.ceil(math.log(N, 2)) + 1
tree = [0] * (2 ** H)
# 세그먼트 트리 만들기
segment_tree(arr, tree, 1, 1, N)
print(tree)

# 합 찾기
left, right = map(int, input().split())
result = find_sum(tree, 1, 1, N, left, right)
print(result)

# 수 변경하기
idx, val = map(int, input().split())
diff = val - arr[idx]
update(tree, 1, 1, N, idx, diff)
print(tree)