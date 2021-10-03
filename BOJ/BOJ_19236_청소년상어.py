# BOJ 19236 청소년 상어

'''
--- 물고기 이동 ---
물고기 번호: 1 ~ 16
물고기 방향: 8방향(상하좌우,대각선)

물고기가 갈 수 있는 칸: 빈칸, 다른 물고기가 있는 칸
물고기가 갈 수 없는 칸: 경계 밖, 상어가 있는 칸

번호가 작은 물고기부터 이동
한번에 한 칸만 이동
각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 회전(반시계)
이동 가능한 방향이 없다면 이동 X

이동할 때는 서로의 위치를 바꾸는 방식

--- 상어 이동 ---
상어의 첫 방향은 0,0에 있는 물고기 방향
여러 칸 이동 가능
이동 후 그 칸에 있는 물고기를 먹고 물고기의 방향을 가진다.
물고기가 없는 칸으로는 이동 불가
상어가 이동 가능한 칸이 없다면 공간에서 벗어나 집으로 간다.
상어 이동 후에는 다시 물고기가 이동한다.

상어가 먹을 수 있는 물고기 번호의 합의 "최댓값"을 구해보자.


접근 방법

1. 재귀 함수
- 상어 이동(이동 가능한 경우가 없을 때 리턴)
- 이동가능한 경우의 수가 여러가지
- 이동 후 물고기 이동함수 호출
- 상어 이동 재귀호출
- 물고기 원래 위치 복귀


물고기 이동을 어떻게 처리할 것인지?

1. 이차원 배열(번호만 저장)
2. info 딕셔너리
- 물고기 위치, 상어 위치 복구시 활용
3. new info 딕셔너리
- 바뀐 물고기 위치, 상어위치 저장 후 재귀호출시 입력
4. 물고기 방향체크 함수
5. 상어 방향체크 함수

'''

N = 4
board = [[0] * N for _ in range(N)]
info = {}
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        n = j * 2
        board[i][j] = line[n]
        info[line[n]] = [i, j, line[n+1]-1]
info['shark'] = [-1, -1, -1]

# 상어 이동방향 체크 함수
def shark_dir(board, info):
    arr = []
    # 상어의 첫 번째 이동인 경우
    if info['shark'][0] == -1:
        arr.append(board[0][0])
    # 이후 이동
    else:
        d = info['shark'][2]
        y, x = info['shark'][:2]
        for i in range(1, 4):
            ny, nx = y + dy[d] * i, x + dx[d] * i
            if 0 <= ny < N and 0 <= nx < N:
                fish = board[ny][nx]
                if fish and fish != 'shark':
                    arr.append(fish)
    return arr

# 물고기 이동 함수
def move_fish(board, info, new_info):
    # 이동 가능한 물고기 체크
    arr = []
    for i in range(N):
        for j in range(N):
            n = board[i][j]
            if n and n != 'shark':
                arr.append(n)
    # 물고기 이동
    arr.sort()
    for a in arr:
        if a in new_info: y, x, d = new_info[a]
        else: y, x, d = info[a]
        # 방향 체크
        for i in range(8):
            nd = (d + i) % 8
            ny, nx = y + dy[nd], x + dx[nd]
            # 가능여부 체크(범위, 물고기, 상어)
            if 0 <= ny < N and 0 <= nx < N:
                fish = board[ny][nx]
                # 물고기라면
                if fish and fish != 'shark':
                    if fish in new_info:
                        fd = new_info[fish][2]
                    else: fd = info[fish][2]
                    new_info[a] = [ny, nx, nd]
                    board[ny][nx] = a
                    new_info[fish] = [y, x, fd]
                    board[y][x] = fish
                    break
                # 빈공간이라면
                if not fish:
                    new_info[a] = [ny, nx, nd]
                    board[y][x] = 0
                    board[ny][nx] = a
                    break
    return

# 재귀 함수
def play(board, info, k):
    global ans
    # 상어가 이동 가능한 방향 체크(가능한 목록 리턴)
    s_arr = shark_dir(board, info)
    # 상어가 이동 가능한 방향이 없다면 리턴
    if not s_arr:
        if k > ans: ans = k
        return
    # 있다면 for문으로 순회
    for i in s_arr:
        new_info = {}
        # 먹을 수 있는 물고기 정보
        y, x, d = info[i]
        # 상어 이동
        board[y][x] = 'shark'
        new_info['shark'] = [y, x, d]
        # 상어 기존위치 비우기
        if 0 <= info['shark'][0] < N:
            sy, sx = info['shark'][:2]
            board[sy][sx] = 0
        # 물고기 이동
        move_fish(board, info, new_info)
        # play함수 재귀 호출
        play(board, new_info, k + i)
        # 물고기 위치, 상어 위치 복구(info 딕셔너리 활용)
        for i in range(N):
            for j in range(N):
                board[i][j] = 0
        for key, value in info.items():
            oy, ox = value[:2]
            board[oy][ox] = key

ans = 0
play(board, info, 0)
print(ans)