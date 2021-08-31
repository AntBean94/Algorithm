# BOJ 10816 숫자 카드 2

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))

dic = {}
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

ans = ""
for i in card:
    if i in dic:
        ans += f'{dic[i]} '
    else:
        ans += '0 '
print(ans)