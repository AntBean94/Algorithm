# BOJ 14503 로봇 청소기

'''
0: 상
1: 우
2: 하
3: 좌

좌표: (0, 0) 좌상단 끝

1. 현재 위치를 청소한다.

2. 


'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Y, X, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 상, 우, 하, 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

clean_status = True
ans = 0
while clean_status:
    # 1. board에서 현재위치 청소
    if board[Y][X] == 0:
        board[Y][X] = 2
        ans += 1
    break_cdn = 0
    # 2. 현재 위치, 방향 기준 왼쪽 방향부터 인접방향 탐색
    for d in range(4):
        # 좌측 탐색
        dir = D - 1
        if D - 1 < 0:
            dir = 3
        r, c = Y + dy[dir], X + dx[dir]
        # 2-1. 왼쪽 방향이 0이면 '회전'하고 1칸 전진 후 (1)로 돌아감
        if board[r][c] == 0:
            D = dir
            Y, X = r, c
            break
        # 2-2. 공간이 없다면 회전하고 2번 다시 반복
        else:
            D = dir
        # 2-3. 네 방향 모두 청소, 벽(0이 없는경우) 바라보는 방향을 유지한채로 한칸 후진 2번 돌아감
        if d == 3:
            r, c = Y - dy[D], X - dx[D]
            # 2-4. 뒤쪽방향이 벽이라 후진도 못하면 작동 중지 
            if board[r][c] == 1:
                break_cdn = 1
            else:
                Y, X = r, c

    if break_cdn:
        clean_status = False

print(ans)