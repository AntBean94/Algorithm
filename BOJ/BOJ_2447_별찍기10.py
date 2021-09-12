# BOJ 2447 별 찍기 - 10
import sys

N = int(input())
board = [[' '] * N for _ in range(N)]

def star(n, y, x):
    # 탈출 조건
    if n == 1:
        board[y][x] = '*'
        return

    k = n // 3
    for i in range(0, n, k):
        for j in range(0, n, k):
            if i // k == 1 and j // k == 1: continue
            star(k, y + i, x + j)

star(N, 0, 0)

ans = ""
for line in board:
    ans += "".join(line) + '\n'
sys.stdout.write(ans)