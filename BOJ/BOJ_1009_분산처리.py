# BOJ 1009 분산처리

import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    a, b = map(int, input().split())
    ans = str(pow(a, b, 10))[-1]
    if ans == '0': print(10)
    else: print(ans)