# BOJ 10844 쉬운 계단 수

'''
0 ~ 9까지
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

[0, 1, 1, 1, 1, 1, 1, 1, 1, 1] => 9
[1, 1, 2, 2, 2, 2, 2, 2, 2, 1] => 17
:
:
:

'''

N = int(input())

arr = [[0] * 10 for _ in range(N + 1)]
# 초기값 세팅
for i in range(1, 10):
    arr[1][i] = 1

dx = [-1, 1]
# 배열 순회
for i in range(1, N):
    for j in range(10):
        for d in range(2):
            x = j + dx[d]
            if 0 <= x < 10:
                arr[i + 1][x] += arr[i][j]

print(sum(arr[N]) % 1000000000)