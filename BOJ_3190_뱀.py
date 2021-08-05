# BOJ 3190 뱀

'''
벽에 부딛히거나 
자기자신의 몸과 부딪히면 게임이 끝난다.
'''

import sys
input = sys.stdin.readline

N = int(input())    # 보드의 크기
K = int(input())    # 사과의 갯수
# 게임판
board = [[0] * N for _ in range(N)]
for _ in range(K):
    i, j = map(int, input().split())
    board[i-1][j-1] = -1

L = int(input())
dir_info = [0] * 10001
for _ in range(L):
    time, d = map(str, input().split())
    dir_info[int(time)] = d
time = 0
# 뱀의 머리 위치
y, x = 0, 0
# 뱀 정보는 queue로 관리
snake = [[y, x]]
board[y][x] = 1
# 델타탐색 (시계방향)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
dir = 1
# 사과 탐색 시작
for t in range(1, 10001):
    time = t
    # 방향에 따른 이동
    x += dx[dir]
    y += dy[dir]
    # 나갔는지 체크
    if (x < 0 or x >= N) or (y < 0 or y >= N):
        break
    # 사과 체크 및 이동
    if board[y][x] < 0:
        snake.append([y, x])
        board[y][x] = 1
    # 사과가 없는 경우
    elif board[y][x] == 0:
        snake.append([y, x])
        board[y][x] = 1
        tale = snake.pop(0)
        i, j = tale[0], tale[1]
        board[i][j] = 0
    # 몸통과 부딪힌경우
    else:
        break
    # 방향체크
    if dir_info[t] == 'D':
        dir += 1
        if dir > 3:
            dir = 0
    elif dir_info[t] == 'L':
        dir -= 1
        if dir < 0:
            dir = 3
print(time)

        
    


