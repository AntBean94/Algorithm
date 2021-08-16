# BOJ 2588 곱셈

A = int(input())
B = input()

for b in B[::-1]:
    print(A*int(b))
print(A*int(B))