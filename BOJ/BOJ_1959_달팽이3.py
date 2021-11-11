# BOJ 1959 달팽이3

'''
수학

정사각형을 기준으로

1. 가로가 짧은 경우
정사각형일때 + 1
좌표는 가로 짝 => 상단
가로 홀 => 하단

2. 가로가 긴 경우
정사각형일때와 같다.
좌표는 세로 짝 => 좌측
좌표는 세로 홀 => 우측
'''

N, M = map(int, input().split())
std = min(N, M)
# 회전 횟수 출력
cnt = 2 * std - 2
c = std // 2 + 1
if std % 2: y, x = c, c
else: y, x = c, c - 1
dif = abs(M - N)
if N > M:
    print(cnt + 1)
    if M % 2: print(y + dif, x)
    else: print(y, x)
else:
    print(cnt)
    if N % 2: print(y, x + dif)
    else: print(y, x)