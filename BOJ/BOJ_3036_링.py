# BOJ 3036 링

N = int(input())
ring = list(map(int, input().split()))

def gcd(n, m):
    if m > n: n, m = m, n
    if m == 0: return n
    if n % m == 0: return m
    else: return gcd(m, n % m)
    
first = ring[0]
for n in ring[1:]:
    # 기약분수 형태(분자, 분모를 최대공약수로 나눈 값)
    g = gcd(first, n)
    print(f'{first//g}/{n//g}')