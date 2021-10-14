# BOJ 9252 LCS 2

A = input()
B = input()

H = len(A)
W = len(B)
table = [[0] * (W + 1) for _ in range(H + 1)]

for i in range(H):
    for j in range(W):
        # 같다면
        if A[i] == B[j]:
            table[i+1][j+1] = table[i][j] + 1
        # 다르다면
        else:
            table[i+1][j+1] = max(table[i+1][j], table[i][j+1])

L = table[H][W]
route = ""
n = L
y, x = H, W
while n != 0:
    # 위로 이동
    while table[y][x] == n:
        y -= 1
    y += 1
    # 좌로 이동
    while table[y][x] == n:
        x -= 1
    x += 1
    route += A[y-1]
    y -= 1
    x -= 1
    n -= 1

print(L)
print(route[::-1])