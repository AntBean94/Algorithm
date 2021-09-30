# BOJ 21609 상어 중학교

'''
검은색 블록, 무지개 블록, 일반 블록

일반 블록: M가지 색상(M이하의 자연수로 표현)
검은색 블록: -1
무지개 블록: 0

인접 조건: 상, 하, 좌, 우

블록 그룹: 연결된 블록의 집합
- 일반 블록이 적어도 하나 있어야 한다.
- 일반 블록의 색은 모두 같아야 한다.
- 검은색 블록은 포함하면 안됨
- 무지개 블록은 상관없음
- 서로 모두 연결되어 있어야 한다.
- 그룹의 크기는 2 이상
- 기준블록은 일반블록중에서 행, 열이 가장 작은 블록(즉, 좌상단)

오토플레이
1. 크기가 가장 큰 블록그룹(같다면 무지개블록, 같다면 기준블록이 가장 큰)
2. 1에서 찾은 블록그룹의 모든 블록 제거(B^2점 획득, B:제거한 블록의 수)
3. 중력 작용
4. 격자가 90도 반시계 방향으로 회전
5. 중력 작용
6. 블록그룹이 존재하는동안 계속 진행

중력 작용
- 행의 번호가 큰 칸으로 이동(비어있는 곳으로)

N = 20
M = 5

400개

블록그룹 확인: bfs

오토 플레이
블록그룹에 해당하는 위치 전부 10으로 변환

반시계 방향 회전

중력 작용

'''
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

point = 0

# 그룹 찾기
def bfs(i, j, color):
    value = []
    rainbow = []
    cnt, total = 0, 0
    vis[i][j] = 1
    Q = deque()
    Q.append([i, j])
    while Q:
        y, x = Q.popleft()
        value.append([y, x])
        total += 1
        if board[y][x] > 0: cnt += 1
        else: rainbow.append([y, x])
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                nxt = board[ny][nx]
                if not vis[ny][nx] and (nxt == 0 or nxt == color):
                    vis[ny][nx] = 1
                    Q.append([ny, nx])
    # 레인보우 블록 방문 제거
    rainbow_cnt = 0
    for y, x in rainbow:
        vis[y][x] = 0
        rainbow_cnt += 1
    # 일반 블록이 1이상이면서 그룹크기 2이상
    if cnt > 0 and total > 1:
        # 최대그룹여부 확인
        if total > max_total:
            return total, rainbow_cnt, value
        elif total == max_total:
            if rainbow_cnt >= max_rainbow_cnt:
                return total, rainbow_cnt, value
    return False, False, False


def gravity(board):
    for j in range(N):
        Q = deque()
        emp = deque()
        for i in range(N-1, -1, -1):
            val = board[i][j]
            if 0 <= val < 10:
                Q.append(val)
                board[i][j] = 10
                emp.append([i, j])
            elif val == 10: emp.append([i, j])
            else:
                while Q:
                    num = Q.popleft()
                    ny, nx = emp.popleft()
                    board[ny][nx] = num
                emp.clear()
        while Q:
            num = Q.popleft()
            ny, nx = emp.popleft()
            board[ny][nx] = num


def rotate(board):
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[N-1-c][r] = board[r][c]
    return ret


while True:
    max_total = 0
    max_rainbow_cnt = 0
    group = []
    # 가장 큰 그룹 결정
    vis = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not vis[i][j] and 0 < board[i][j] < 10:
                # 그룹 찾기 함수 실행
                total, rainbow_cnt, value = bfs(i, j, board[i][j])
                if not total: continue
                max_total = total
                max_rainbow_cnt = rainbow_cnt
                group = value

    # 그룹이 없다면 멈춘다.
    if not max_total: break

    # 가장 큰 그룹 제거
    for i, j in group:
        board[i][j] = 10
    point += max_total ** 2

    # 중력 작용
    gravity(board)

    # 회전(반시계방향 90도)
    board = rotate(board)

    # 중력 작용
    gravity(board)


print(point)