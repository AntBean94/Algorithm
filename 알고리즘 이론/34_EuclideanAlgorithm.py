# 34 유클리드 호제법 (Euclidean Algorithm)

def gcd(m, n):
    if m < n:
        m, n = n, m
    if n == 0: return m
    if m % n == 0: return n
    else: return gcd(m, m%n)