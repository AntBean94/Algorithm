# BOJ 1166 선물

'''
l, r 범위는 0.0000000001 ~ 1000000000
'''

N, L, W, H = map(int, input().split())
l, r = 0.00000000001, 1000000000
while l <= r - r * 0.0000000001:
    m = (l + r) / 2
    a = L // m
    b = W // m
    c = H // m
    if a * b * c >= N:
        l = m
    else:
        r = m
print(m)