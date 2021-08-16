# BOJ 10869 사칙연산

A, B = map(int, input().split())
cal = [A+B, A-B, A*B, A//B, A%B]
for c in cal:
    print(c)
