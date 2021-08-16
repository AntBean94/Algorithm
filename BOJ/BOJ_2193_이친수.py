# BOJ 2193 이친수

# DP 예시(피보나치 수열-보텀 업)
'''
n번째 피보나치 수열을 계산해보시오.

d = [0] * 100
d[1] = 1
d[2] = 1

for i in range(3, n + 1):
    d[i] = d[i-1] + d[i-2]

print(d[n])
'''

N = int(input())
d = [0] * 100
d[1] = 1
d[2] = 1

for i in range(3, N+1):
    d[i] = d[i-1] + d[i-2]

print(d[N])