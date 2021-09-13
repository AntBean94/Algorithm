# BOJ 13460 구슬 탈출 2

'''
4가지 방향으로 10번 => 2^20 = 약 100만개 경우의 수
즉, 완탐도 가능할 듯?

10번 이하로 불가능하다면 -1을 출력한다.
'''

N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]
red, blue = [], []
ans = 11
# 보드 정보 입력
for i in range(N):
    info = input()
    for j in range(M):
        if info[j] == '#': board[i][j] = 1
        elif info[j] == '.': board[i][j] = 0
        elif info[j] == 'O': board[i][j] = 2
        elif info[j] == 'R': red = [i, j]
        else: blue = [i, j]

board[red[0]][red[1]] = 'R'
board[blue[0]][blue[1]] = 'B'
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def move(ball, y, x, d):
    # 현재위치가 구멍이면 바로 리턴
    if board[y][x] == 2:
        return y, x, True
    check = False
    # 공 위치도 바꿔줘야한다.
    board[y][x] = 0
    ny, nx = y, x
    while True:
        ny += dy[d]
        nx += dx[d]
        sig = board[ny][nx]
        if sig == 0: continue
        else:
            if sig == 2:
                check = True
            else:
                ny, nx = ny - dy[d], nx - dx[d]
                board[ny][nx] = ball
            break

    # 이후 바뀐 공위치 리턴
    return ny, nx, check

def game(ry, rx, by, bx, k):
    global ans
    # 탈출 조건(백 트래킹)
    if k >= ans: 
        return

    # 4방향 이동
    for d in range(4):
        nry, nrx, check_r = move('R', ry, rx, d)
        # 공이 빠졌는지 확인
        nby, nbx, check_b = move('B', by, bx, d)
        # 파란공이 움직인 후 빨간 공이 한번 더 움직이는지 확인
        nry, nrx, check_r = move('R', nry, nrx, d)
        # 빨간 공만 빠졌다면 최솟값 갱신 후 리턴
        if check_r and not check_b:
            if k < ans:
                ans = k
        # 파란공이 빠졌다면 되돌리기 위해 리턴
        elif check_b:
            pass
        else:
            # 빠지지 않았다면 재귀 함수
            game(nry, nrx, nby, nbx, k + 1)

        # 재귀 함수 종료 후 좌표 복구
        if not check_r: board[nry][nrx] = 0
        if not check_b: board[nby][nbx] = 0

        board[ry][rx] = 'R'
        board[by][bx] = 'B'


game(red[0], red[1], blue[0], blue[1], 1)
if ans == 11: print(-1)
else: print(ans)