# BOJ 9663 N-Queen

'''
대표적인 백트래킹 문제

퀸을 놓았을때 다음 퀸을 놓을 위치를 잡아야 한다.

기존 퀸 기준 평행선, 수직선, 대각선 위치에는 다른 퀸을 놓을 수 없다.

0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
'''

N = int(input())
board = [[0] * N for _ in range(N)]
ans = 0
col = [0] * N
# 방향 체크
dy = [-1, 1, 1, -1]
dx = [1, 1, -1, -1]

def check(board, y, x):
    # 대각선 체크
    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        while True:
            if 0 <= ny < N and 0 <= nx < N:
                if board[ny][nx]: return False
                ny += dy[d]
                nx += dx[d]
            else: break
    return True

def back_t(board, y):
    global ans
    if y == N:
        ans += 1
        return
    
    for x in range(N):
        if not col[x] and check(board, y, x):
            col[x] = 1
            board[y][x] = 1
            # 재귀
            back_t(board, y + 1) 
            # 탈출
            col[x] = 0
            board[y][x] = 0

back_t(board, 0)
print(ans)