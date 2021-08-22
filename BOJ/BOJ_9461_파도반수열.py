# BOJ 9461 파도반 수열


'''
A[n] = A[n-1] + A[n-]

1 1
2 1
3 1
4 2 (1, 3)
5 2 (4)
6 3 (5, 1)
7 4 (6, 2)
8 5 (7, 3)
9 7 (8, 4)
10 9 (9, 5)

A[n] = A[n-1] + A[n-5]

if A[n-5] < 0:

'''
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [0] * 101
    for i in range(1, N + 1):
        if i < 4:
            arr[i] = 1
        elif i == 4:
            arr[i] = 2
        elif i == 5:
            arr[i] = 2
        else:
            arr[i] = arr[i - 1] + arr[i - 5]
    print(arr[N])