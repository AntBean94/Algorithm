# BOJ 1037 약수

N = int(input())
factor = sorted(list(map(int, input().split())))
print(factor[0] * factor[-1])