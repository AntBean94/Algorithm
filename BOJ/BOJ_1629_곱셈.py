# BOJ 1629 곱셈

a, b, c = map(int, input().split())

def multiple(a, b, c):
    if b == 0: return 1
    if b == 1: return a % c
    if not (b % 2):
        tmp = multiple(a, b / 2, c)
        return (tmp * tmp) % c
    else:
        tmp = multiple(a, b - 1, c)
        return (a * tmp) % c

ans = multiple(a, b, c)
print(ans)