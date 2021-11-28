# BOJ 11659 구간 합 구하기 4

'''
prefix sum
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
# 누적합 구하기
prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = arr[i - 1] + prefix[i - 1]
# 부분합 출력
for i in range(M):
    a, b = map(int, input().split())
    print(prefix[b] - prefix[a - 1])