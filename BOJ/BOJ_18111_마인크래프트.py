# BOJ 18111 마인크래프트

'''
제거: 2초
쌓기: 1초

맵의 크기
높이: 256블록
넓이: 500 * 500 = 250,000

접근법
가능한 가장 높은 위치에서부터 

현재 높이별 블록 갯수
[1, 100, 20, 41, ...]
256으로 한정지을 수 있음
256개의 케이스중에서
위부터 아래로 가능한 케이스중 가장 작은 케이스
'''

N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
H = [0] * 257
mh, nh = 0, 1000
for i in range(N):
    for j in range(M):
        h = ground[i][j]
        H[h] += 1
        if h > mh: mh = h
        if h < nh: nh = h
# 시간, 땅 높이
ans = [100000000, 0]
for i in range(mh, nh - 1, -1):
    t, b = 0, B
    for h, cnt in enumerate(H):
        if h < i:
            t += cnt * (i - h)
            b -= cnt * (i - h)
        elif h > i:
            t += 2 * cnt * (h - i)
            b += cnt * (h - i)
    if b >= 0 and t < ans[0]:
        ans = [t, i]
print(*ans)