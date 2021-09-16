# BOJ 2981 검문

'''
접근 방법

8, 103, 38

8 보다 큰 경우 최대 가능한 나머지는 8이다.

2, 2, 2

103

2, 19

M < 두번째로 작은 수
가능한 나머지 범위 <= 가장 작은 수

최대 공약수: 1

1을 뺀 수가 서로 최대 공약수를 가지는지?
2을 뺀 수가 서로 최대 공약수를 가지는지?
3을 뺀 수가 서로 최대 공약수를 가지는지?

8, 38
2, 3, 5, 6, 15, 30

30
2, 3, 5, 6, 15, 30

30, 65, 95

차이의 최대 공약수가 중요
'''
import sys
import math
input = sys.stdin.readline

N = int(input())
arr = []
arr_dist = set()
for i in range(N):
    n = int(input())
    if arr:
        for a in arr:
            arr_dist.add(abs(n - a))
    arr.append(n)

def gcd(m, n):
    if m < n:
        m, n = n, m
    if n == 0: return m
    if m % n == 0: return n
    else: return gcd(m, m%n)

# 최대 공약수 뽑기
num = 0
for n in arr_dist:
    if not num: num = n
    else: num = gcd(num, n)

ans = set([num])
for i in range(2, int(math.sqrt(num)) + 2):
    if not num % i: 
        ans.add(i)
        ans.add(num // i)

print(*sorted(ans))