# BOJ 9020 골드바흐의 추측

num = [1] * (10001)
for i in range(2, int(len(num)**0.5)):
    if num[i]:
        n = 2
        while i * n <= len(num)-1:
            num[i * n] = 0 
            n += 1

for _ in range(int(input())):
    N = int(input())
    a = 0
    b = 0
    for i in range(N//2, 0, -1):
        if num[i]:
            for j in range(N, N//2-1, -1):
                if num[j]:
                    if i + j == N:
                        a = i
                        b = j
                        break
        if a and b:
            break

    print(a, b)