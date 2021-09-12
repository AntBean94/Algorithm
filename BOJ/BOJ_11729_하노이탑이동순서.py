# BOJ 11729 하노이 탑 이동 순서

import sys

N = int(input())

print(2 ** N - 1)
def hanoi(n, fo, to, vi):
    if n == 1: print(fo, to)
    else:
        hanoi(n - 1, fo, vi, to)
        print(fo, to)
        hanoi(n - 1, vi, to, fo)
hanoi(N, 1, 3, 2)