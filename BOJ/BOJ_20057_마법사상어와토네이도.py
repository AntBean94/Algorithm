# BOJ 20057 마법사 상어와 토네이도

'''
접근 방법

격자의 바깥으로 나간 모래의 양을 구해보자

500 * 500 = 250,000
250,000 * 10 = 2,500,000
=> 완전탐색 가능

방향과 위치를 곱해서 계산

방향
좌, 하, 우, 상
[(0, -1), (1, 0), (0, 1), (-1, 0)]

자기 기준 좌회전(방향 1증가) 또는 직진(방문 기록, 자기방향)

5, 5 (0, -1)

[5%]
r + d1 * 2, c + d2 * 2
[2%]
r - (1 - d1)(1 + d2) * 2, c - (1 - d1)(1 + d2) * 2
r + (1-d1)(1+d2)*2, c + (1-d1)(1+d2)*2
[7%]
r - (1-d1)(1+d2), c - (1-d1)(1+d2)
r + (1-d1)(1+d2), c + (1-d1)(1+d2)
[10%]
r + d + (1 - d)(1 + d), c + d + (1 - d)(1 + d)
r + d - (1 - d)(1 + d), c + d - (1 - d)(1 + d)
[1%]
r - d + (1 - d)(1 + d), c - d + (1 - d)(1 + d)
r - d - (1 - d)(1 + d), c - d - (1 - d)(1 + d)
[a]
r + d, c + d

로직
- while문으로 1,1까지 실행
- 방향 d = 0부터 시작
- 왼쪽 회전이 가능한경우(방문 체크) 왼쪽회전(방향 1 증가)
- 회전이 불가능한 경우 직진(방향 유지)
- 바뀐 위치와 방향을 토네이도 함수에 넣는다.
- 토네이도 함수에서는 배열을 변화시키며 배열 밖으로 날라간 먼지를 반환한다.
- 반복

'''

import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ong = 0
for b in board:
    ong += sum(b)

# 좌, 하, 우, 상
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

# 토네이도
def tornado(board, y, x, d1, d2):
    total = board[y][x]
    a = 0
    oom = 0
    # 기준점 모래 날리기
    board[y][x] = 0
    # 5%
    tmp = int(total * 0.05)
    a += tmp
    ny, nx = y+d1*2, x+d2*2
    if 0 <= ny < N and 0 <= nx < N:
        board[ny][nx] += tmp
    else: oom += tmp
    # 2%
    tmp = int(total * 0.02)
    a += 2 * tmp
    ny, nx = y-(1-d1)*(1+d1)*2, x-(1-d2)*(1+d2)*2
    if 0 <= ny < N and 0 <= nx < N:
        board[ny][nx] += tmp
    else: oom += tmp
    ny, nx = y+(1-d1)*(1+d1)*2, x+(1-d2)*(1+d2)*2
    if 0 <= ny < N and 0 <= nx < N:
        board[ny][nx] += tmp
    else: oom += tmp
    # 7%
    tmp = int(total * 0.07)
    a += 2 * tmp
    ny, nx = y-(1-d1)*(1+d1), x-(1-d2)*(1+d2)
    if 0 <= ny < N and 0 <= nx < N:
        board[ny][nx] += tmp
    else: oom += tmp
    ny, nx = y+(1-d1)*(1+d1), x+(1-d2)*(1+d2)
    if 0 <= ny < N and 0 <= nx < N:
        board[ny][nx] += tmp
    else: oom += tmp
    # 10%
    tmp = int(total * 0.1)
    a += 2 * tmp
    ny, nx = y+d1+(1-d1)*(1+d1), x+d2+(1-d2)*(1+d2)
    if 0 <= ny < N and 0 <= nx < N:
        board[ny][nx] += tmp
    else: oom += tmp
    ny, nx = y+d1-(1-d1)*(1+d1), x+d2-(1-d2)*(1+d2)
    if 0 <= ny < N and 0 <= nx < N:
        board[ny][nx] += tmp
    else: oom += tmp
    # 1%
    tmp = int(total * 0.01)
    a += 2 * tmp
    ny, nx = y-d1+(1-d1)*(1+d1), x-d2+(1-d2)*(1+d2)
    if 0 <= ny < N and 0 <= nx < N:
        board[ny][nx] += tmp
    else: oom += tmp
    ny, nx = y-d1-(1-d1)*(1+d1), x-d2-(1-d2)*(1+d2)
    if 0 <= ny < N and 0 <= nx < N:
        board[ny][nx] += tmp
    else: oom += tmp
    # a%
    tmp = total - a
    ny, nx = y + d1, x + d2
    if 0 <= ny < N and 0 <= nx < N:
        board[ny][nx] += tmp
    else: oom += tmp

    return oom

result = 0
vis = [[0] * N for _ in range(N)]
y, x = N // 2, N // 2
vis[y][x] = 1
d = 0

while True:
    # 시작케이스
    if y == N // 2 and x == N // 2:
        y, x = y + dy[d], x + dx[d]
    else:
        # 왼쪽 확인
        nd = (d + 1) % 4
        ny, nx = y + dy[nd], x + dx[nd]
        if vis[ny][nx]:
            y, x = y + dy[d], x + dx[d]
        else: y, x, d = ny, nx, nd
    vis[y][x] = 1
    
    # 토네이도
    result += tornado(board, y, x, dy[d], dx[d])

    # 종료 조건
    if y == 0 and x == 0: break

print(result)