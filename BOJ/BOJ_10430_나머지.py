# BOJ 10430 나머지

A, B, C = map(int, input().split())
cal = [(A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C]
for c in cal:
    print(c)