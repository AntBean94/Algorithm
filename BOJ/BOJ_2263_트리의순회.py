# BOJ 2263 트리의 순회

'''
중위 순회, 후위 순회가 주어졌을 때 전위순회를 구하는 문제

A: 4 2 5 1 3
B: 4 5 2 3 1

1. B의 가장 우측값 체크(우측값 출력)
2. A에서 그 값의 인덱스를 찾는다.
- 그 값을 기준으로 좌, 우 분할
- 각 위치의 가장 우측인덱스를 1에 전달
'''
import sys
sys.setrecursionlimit(150000)

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
T = [0] * (N + 1)
for i, n in enumerate(inorder): T[n] = i

def find_pre(il, ir, pl, pr):
    if il == ir: return
    # 출력
    n = postorder[pr-1]
    print(n, end=" ")

    # A에서 n의 인덱스 찾기
    idx = T[n]
    find_pre(il, idx, pl, pl + idx - il)
    find_pre(idx + 1, ir, pl + idx - il, pr - 1)

find_pre(0, N, 0, N)