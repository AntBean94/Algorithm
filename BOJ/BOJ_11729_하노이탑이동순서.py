# BOJ 11729 하노이 탑 이동 순서

import sys

N = int(input())
table = [list([""] * (4) for _ in range(4)) for _ in range(N + 1)]

print(2 ** N - 1)
def hanoi(n, fo, to, vi):
    global ans
    if n == 1: return f"{fo} {to}\n"
    if table[n][fo][to]:
        return table[n][fo][to]
    else:
        tmp = ""
        tmp += hanoi(n - 1, fo, vi, to)
        tmp += f"{fo} {to}\n"
        tmp += hanoi(n - 1, vi, to, fo)
        return tmp
        
ans = hanoi(N, 1, 3, 2)
sys.stdout.write(ans)