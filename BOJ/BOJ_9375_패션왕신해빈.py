# BOJ 9375 패션왕 신해빈

T = int(input())
for tc in range(T):
    N = int(input())
    cloth = {}
    for i in range(N):
        a, b = map(str, input().split())
        if b in cloth: cloth[b] += 1
        else: cloth[b] = 1
    ans = 1
    for i in cloth:
        ans *= (cloth[i] + 1)
    print(ans - 1)