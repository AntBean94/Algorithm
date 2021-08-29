# BOJ 10830 행렬 제곱

'''
접근법

A^B

i) B % 2 = 0 (짝수)
A^B = A^(1/2)B * A^(1/2)B

ii) B % 2 = 1 (홀수)
A^B = A * A^(B-1)

iii) B = 1
A^B = A

'''

import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
K = 0
# 행렬 곱 함수
def multiple(arr_a, arr_b):
    global K
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result = 0
            for k in range(N):
                result += arr_a[i][k] * arr_b[k][j]
            arr[i][j] = result % 1000
    return arr

# 분할 정복
def find_matrix(arr, b):
    # print(b)
    if b == 1:
        return arr
    # 홀수인경우
    elif bin(b)[-1] == "1":
        print(b)
        return multiple(arr, find_matrix(arr, b-1))
    # 짝수인경우
    else:
        result = find_matrix(arr, b // 2)
        return multiple(result, result)

ans = find_matrix(A, B)
for ro in ans:
    for r in ro:
        print(r % 1000, end=" ")
    print()