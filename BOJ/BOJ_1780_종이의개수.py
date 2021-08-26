# BOJ 1780 종이의 개수

import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

def check(arr, y, x, l):
    if l == 1: return True
    std = arr[y][x]
    for i in range(y, y + l):
        for j in range(x, x + l):
            if arr[i][j] != std:
                return False
    return True

def divide(arr, y, x, l):
    if check(arr, y, x, l):
        ans[arr[y][x]] += 1
    else:
        nl = l // 3
        divide(arr, y, x, nl)
        divide(arr, y, x + nl, nl)
        divide(arr, y, x + 2 * nl, nl)
        divide(arr, y + nl, x, nl)
        divide(arr, y + 2 * nl, x, nl)
        divide(arr, y + nl, x + nl, nl)
        divide(arr, y + 2 * nl, x + nl, nl)
        divide(arr, y + nl, x + 2 * nl, nl)
        divide(arr, y + 2 * nl, x + 2 * nl, nl)

ans = [0, 0, 0]

divide(paper, 0, 0, N)
print(ans[-1], end=" ")
print(*ans[:-1])