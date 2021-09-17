# BOJ 17144 미세먼지 안녕 !

import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
# 공기 청정기 위치 확인
lmt = []
for i in range(R):
    if board[i][0] == -1: 
        lmt = [i, i + 1]
        break
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
dir = [
    [0, 1, 2, 3],
    [2, 1, 0, 3]
]

for t in range(T):
    # 미세먼지 확산
    spread = []
    for i in range(R):
        for j in range(C):
            value = board[i][j]
            # 0또는 공기청정기이면 생략
            if value < 1: continue
            # 4방면으로 확산
            cnt = 0
            dust = int(value / 5)
            if not dust: continue
            for d in range(4):
                ny, nx = i + dy[d], j + dx[d]
                if 0 <= ny < R and 0 <= nx < C and board[ny][nx] > -1:
                    cnt += 1
                    spread.append([dust, ny, nx])
            # 미세먼지 감소
            board[i][j] -= cnt * dust

    for dust, y, x in spread:
        board[y][x] += dust

    dmt = [
        [0, lmt[1]],
        [lmt[1], R]
    ]
    # 공기 순환
    for i in range(2):
        y, x = lmt[i], 0
        pre = []
        for d in dir[i]:
            while True:
                y += dy[d]
                x += dx[d]
                if dmt[i][0] <= y < dmt[i][1] and 0 <= x < C:
                    # 숫자를 옮긴다.
                    if board[y][x] == -1:
                        if pre: 
                            board[pre[0]][pre[1]] = 0
                            break
                        else: continue
                    if pre:
                        board[pre[0]][pre[1]] = board[y][x]
                    pre = [y, x]
                else:
                    # 되돌리고 중단
                    y -= dy[d]
                    x -= dx[d]
                    break
        board[pre[0]][pre[1]] = 0

# 미세먼지 갯수 체크
ans = 0
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            ans += board[i][j]

print(ans)