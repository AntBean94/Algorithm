# BOJ 2742 피보나치 수 2

'''
bottom-up
'''

N = int(input())
DP = [0] * 100
DP[1], DP[2] = 1, 1
for i in range(2, N + 1):
    DP[i] = DP[i - 1] + DP[i - 2]
print(DP[N])