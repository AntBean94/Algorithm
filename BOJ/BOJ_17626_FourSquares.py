# BOJ 17626 Four Squares

'''
라그랑주

100이면 10이하의 합성수

50000이면 약 200~250이하의 합성수

자체가 제곱수인 경우
그 외에는 합성수
'''

N = int(input())
DP = [0] * (N + 1)
DP[1] = 1
for i in range(2, N + 1):
    tmp = 10000
    for j in range(1, int(i ** 0.5) + 1):
        tmp = min(tmp, DP[i - j * j])
    DP[i] = tmp + 1
print(DP[N])