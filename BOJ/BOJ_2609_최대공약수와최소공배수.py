# BOJ 2609 최대공약수와 최소공배수

num = list(map(int, input().split()))
N = max(num)

factors = [[0] * 10001 for _ in range(2)]

for i in range(2):
    n = num[i]
    while n != 1:
        for j in range(2, n + 1):
            if not n % j: 
                n //= j
                factors[i][j] += 1
                break

gcd = [0] * 10001
lcm = [0] * 10001
for i in range(2, N + 1):
    gcd[i] = min(factors[0][i], factors[1][i])
    lcm[i] = max(factors[0][i], factors[1][i])

ans_g = 1
for i in range(2, N + 1):
    if gcd[i]: ans_g *= i ** gcd[i]

ans_l = 1
for i in range(2, N + 1):
    if lcm[i]: ans_l *= i ** lcm[i]
print(ans_g)
print(ans_l)