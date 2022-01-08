# BOJ 1965 상자넣기

'''
가장 긴 증가수열 문제

방법 1. DP
O(n^2)

방법 2. 이분탐색
O(n log n)
'''

N = int(input())
box = list(map(int, input().split()))

def solution_dp():
    DP = [1] * N
    for i in range(N):
        n = box[i]
        for j in range(i + 1, N):
            m = box[j]
            if m < n and DP[j] >= DP[i]: break
            if n < box[j]:
                DP[j] = max(DP[j], DP[i] + 1)
    print(max(DP))
solution_dp()

def solution_bs():
    from bisect import bisect_left as bl
    arr = []
    lth = 0
    for i in range(N):
        n = box[i]
        idx = bl(arr, n)
        if idx == lth:
            lth += 1
            arr.append(n)
        elif n < arr[idx]:
            arr[idx] = n
    print(lth)
solution_bs()