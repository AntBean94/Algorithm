# BOJ 2263 트리의 순회

'''
중위 순회, 후위 순회가 주어졌을 때 전위순회를 구하는 문제

1 2 3
1 3 2



A: 4 2 5 1 3
B: 4 5 2 3 1

1. B의 가장 우측값 체크(우측값 출력)
2. A에서 그 값의 인덱스를 찾는다.
- 그 값을 기준으로 좌, 우 분할
- 각 위치의 가장 우측인덱스를 1에 전달



1 2 4 5 3

'''

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

def find_post(l, r):
    # 출력
    print(postorder[l:r][-1], end=" ")

    # 분할 정복
    



find_post(0, N)