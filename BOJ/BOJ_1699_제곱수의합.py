# BOJ 1699 제곱수의 합

'''
bottom-up
'''

N = int(input())
DP = [0] * (N + 1)
S = [i * i for i in range(1, 317)]
for i in range(1, N + 1):
    tmp = []
    for j in S:
        if j > i: break
        tmp.append(DP[i - j])
    DP[i] = min(tmp) + 1
print(DP[N])