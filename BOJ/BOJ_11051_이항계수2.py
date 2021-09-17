# BOJ 11051 이항 계수 2

'''
페르마의 소정리
'''
N, K = map(int, input().split())
P = 10007
if N - K < K: K = N - K
top = 1
for i in range(N - K + 1, N + 1):
    top *= i
    top %= 10007

bot = 1
for i in range(2, K + 1):
    bot *= i
    bot %= 10007

def mul(b, r, p):
    c = 1
    while r > 0:
        # 홀수인경우
        if bin(r)[-1] == '1':
            c *= b
            c %= p
        b *= b
        b %= p
        r //= 2
    return c

# 모듈로 곱셈의 역원
rev = mul(bot, P - 2, P)

print((top * rev) % 10007)