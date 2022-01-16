# BOJ 15988 1, 2, 3 더하기 3

'''
점화식
DP[n] = DP[n-1] + DP[n-2] + DP[n-3]
'''

import sys
input = sys.stdin.readline

T = int(input())
test_case = [int(input()) for _ in range(T)]
n = max(test_case)
DP = [0] * (n + 1)
DP[:3] = [1, 1, 2]
for i in range(3, n + 1):
    DP[i] = sum(DP[i-3:i]) % 1000000009
for tc in test_case:
    print(DP[tc])