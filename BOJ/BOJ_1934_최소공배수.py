# BOJ 1934 최소공배수

import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    num = sorted(list(map(int, input().split())))
    a, b = num[0], num[1]
    gcd = 1
    # 최대공약수를 구하고
    while True:
        if not b % a: 
            gcd = a
            break
        else:
            c = b % a
            a, b = c, a
    # a에 b를 최대공약수로 나눈 몫을 곱한다.
    print(num[0] * (num[1] // gcd))