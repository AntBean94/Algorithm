# BOJ 9095 1, 2, 3 더하기

T = int(input())
for tc in range(T):
    n = int(input())
    arr = [0] * (n + 1)
    for i in range(1, 4):
        if i <= n: arr[i] = 1
    for i in range(n):
        for j in range(1, 4):
            if i + j < n + 1:
                arr[i + j] += arr[i]
    print(arr[-1])