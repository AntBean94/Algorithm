# BOJ 1965 상자넣기

'''
가장 긴 증가수열 문제
'''

N = int(input())
box = list(map(int, input().split()))
DP = [1] * N
for i in range(N):
    n = box[i]
    for j in range(i + 1, N):
        m = box[j]
        if m < n and DP[j] >= DP[i]: break
        if n < box[j]:
            DP[j] = max(DP[j], DP[i] + 1)
print(max(DP))