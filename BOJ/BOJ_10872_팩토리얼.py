# BOJ 10872 팩토리얼

N = int(input())

def f(n):
    if n==1 or n==0:
        return 1
    return f(n-1) * n

print(f(N))