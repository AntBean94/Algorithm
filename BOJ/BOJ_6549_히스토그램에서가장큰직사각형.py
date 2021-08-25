# BOJ 6549 히스토그램에서 가장 큰 직사각형

'''
최솟값의 인덱스를 기록하는 세그먼트 트리 구현

필요 함수
1. 세그먼트 트리 만들기 (최솟값의 인덱스)

2. 최솟값의 인덱스를 찾는 함수

알고리즘
1. 초기값 입력

2. 조건을 바탕으로 최솟값의 인덱스를 기록하는 세그먼트 트리 구현

3. 분할정복 알고리즘
 - if start == end: return
 - 최솟값의 인덱스 찾기(함수 호출)
 - 결과 = 최솟값 X 범위
 - 재귀 호출 결과 = max(왼쪽 범위, 오른쪽 범위)
 return (결과, 재귀 호출 결과)


'''

import sys, math
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
INF = 1000000001
def segment_tree(arr, tree, node, start, end):
    if start == end:
        # 세그먼트 트리에 인덱스를 기록
        tree[node] = start
        return tree[node]
    else:
        # 각 인덱스의 값을 비교하고 더 작은 값을 가진 인덱스를 기록
        left_idx = segment_tree(arr, tree, node*2, start, (start+end)//2)
        right_idx = segment_tree(arr, tree, node*2+1, (start+end)//2+1, end)
        if arr[left_idx] <= arr[right_idx]: tree[node] = left_idx
        else: tree[node] = right_idx
        return tree[node]

def find_min(tree, node, start, end, left, right):
    if left > end or right < start: return INF
    elif left <= start and end <= right: return tree[node]
    else:
        left_idx = find_min(tree, node*2, start, (start+end)//2, left, right)
        right_idx = find_min(tree, node*2+1, (start+end)//2+1, end, left, right)
        if left_idx == INF: return right_idx
        elif right_idx == INF: return left_idx
        if arr[left_idx] <= arr[right_idx]: return left_idx
        else: return right_idx

def find_area(arr, tree, start, end):
    if start == end: return arr[start]
    # 최솟값 찾기
    min_idx = find_min(tree, 1, 1, N, start, end)
    area = (end - start + 1) * arr[min_idx]
    if min_idx == start: sub_area = find_area(arr, tree, min_idx+1, end)
    elif min_idx == end: sub_area = find_area(arr, tree, start, min_idx-1)
    else: sub_area = max(find_area(arr, tree, start, min_idx-1), find_area(arr, tree, min_idx+1, end))
    return max(area, sub_area)

# 테스트케이스 반복
while True:
    arr = list(map(int, input().split()))
    N = arr[0]
    if not N: break
    ''' -----------시작---------- '''
    H = math.ceil(math.log(N, 2)) + 1
    tree = [0] * (2 ** H)
    # 세그먼트 트리 구현
    segment_tree(arr, tree, 1, 1, N)
    # 분할 정복 알고리즘
    result = find_area(arr, tree, 1, N)
    print(result)