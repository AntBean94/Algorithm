# BOJ 11057 오르막 수

'''
n으로 끝나는 오르막 수의 합
DP[n] = sum(DP[:n+1])
'''

N = int(input())
DP = [1] * 10
for i in range(N - 1):
    for j in range(9, -1, -1):
        DP[j] = sum(DP[:j+1])
print(sum(DP) % 10007)