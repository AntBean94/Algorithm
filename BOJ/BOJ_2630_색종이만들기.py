# BOJ 2630 색종이 만들기

import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

def check(arr, y, x, l):
    pivot = arr[y][x]
    for i in range(y, y + l):
        for j in range(x, x + l):
            if arr[i][j] != pivot:
                return False
    return True

def cut_paper(arr, y, x, l):
    global white, blue
    if l == 1:
        if arr[y][x]: blue += 1
        else: white += 1
        return
    elif check(arr, y, x, l):
        if arr[y][x]: blue += 1
        else: white += 1
        return
    else:
        h = l // 2
        cut_paper(arr, y, x, h)
        cut_paper(arr, y, x + h, h)
        cut_paper(arr, y + h, x, h)
        cut_paper(arr, y + h, x + h, h)

white, blue = 0, 0
cut_paper(paper, 0, 0, N)
print(white)
print(blue)