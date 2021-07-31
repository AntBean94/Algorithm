# 17강 에라토스테네스의 체 (Sieve of Eratosthenes) 예제

import sys

n = int(input())
arr = [i for i in range(n+1)]
for i in range(2, n+1):
    k = 2
    if arr[i] == 0:
        continue
    else:
        while i * k <= n:
            arr[i*k] = 0
            k += 1
def f(x):
    return x > 0
sys.stdout.write(" ".join(map(str, filter(f, arr))))