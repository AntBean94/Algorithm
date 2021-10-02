# BOJ 20061 모노미노도미노 2

'''
구현해야 할 함수 목록
1. 수직, 수평 좌표 변환 함수
- 수직, 수평 배열을 모두 수직으로 처리하기 위해
- 

2. 블럭 배치 함수
- 블럭의 종류와 위치가 주어졌을 때, 배열의 아래로 이동시키는 함수
- 배열의 가장 높은위치에 배치

3. 점수 확인 여부 함수
- 블럭 배치 후 점수 체크
- 블럭 배치함수에서 반환한 높이만 체크
- 해당 높이가 다 찼으면 0으로 변환
- 점수 와 높이 반환 (0 or 1 or 2)

4. 블럭 위치 변경 함수
- 3번 함수에서 True(1, 2)를 반환하면 실행
- 점수 변환된 배열 위의 블럭들을 점수만큼 내린다.

=> 4, 5 반복(3번에서 False를 반환할 때 까지)

5. 높이 초과여부 확인 함수
- 0번행과 1번행 확인
- 값이 있다면 모든원소 위치 이동

블럭을 놓은 횟수 = 10,000
블럭 탐색 = 48 * N

'''

import sys
input = sys.stdin.readline

# 두개의 보드
board_g = [[0] * 4 for _ in range(6)]
board_b = [[0] * 4 for _ in range(6)]

# 블럭, 좌표 변환 함수
def trans(t, y, x):
    # 블럭 변환
    if t == 2: t = 3
    elif t == 3: t = 2
    # 기준좌표 변환
    if t == 2: y, x = x, 2 - y
    else: y, x = x, 3 - y
    return t, y, x

# 블럭 배치 함수
def locate(board, t, x):
    h = []
    # 1, 3번 블록(1개 열 확인)
    if t == 1 or t == 3:
        tmp = 0
        for i in range(6):
            if not board[i][x]:
                tmp = i
            else: break
        h.append(tmp)
        h.append(tmp - 1)
        if t == 1:
            board[tmp][x] = 1
        else:
            board[tmp][x] = 1
            board[tmp - 1][x] = 1
    # 2번 블록(2개 열 확인)
    else:
        tmp = [0, 0]
        for k in range(2):
            for i in range(6):
                if not board[i][x+k]:
                    tmp[k] = i
                else: break
        tmp = min(tmp)
        h.append(tmp)
        board[tmp][x] = 1
        board[tmp][x + 1] = 1
    # 배치한 높이 리턴
    return h

# 점수 확인 함수
def check_point(board, height_arr):
    point = 0
    h = []
    # 라인 확인
    for j in height_arr:
        cnt = 0
        for i in range(4):
            if not board[j][i]: 
                cnt += 1
                break
        if not cnt: 
            h.append(j)
            point += 1
    # 0으로 변환
    for j in h:
        for i in range(4):
            board[j][i] = 0
    return point, h

# 블럭 이동
def move_block(board, height, m):
    # 중간 블럭 삭제된 경우
    if m:
        # 사라진 줄의 갯수
        h = len(height)
        t = max(height)
        # 블럭 이동
        for i in range(t - h, -1, -1):
            for j in range(4):
                board[i + h][j] = board[i][j]
                board[i][j] = 0
    # 가장 밑에있는 블럭을 삭제 후 이동
    else:
        # 블럭 삭제
        for i in range(5, 5 - height, -1):
            for j in range(4):
                board[i][j] = 0
        # 블럭 이동
        for i in range(5, 1, -1):
            for j in range(4):
                board[i][j] = board[i - height][j]
                board[i - height][j] = 0

# 초과 블럭 확인
def check(board):
    for i in range(2):
        for j in range(4):
            if board[i][j]:
                if i: return 1
                else: return 2

ans = 0
N = int(input())
for _ in range(N):
    t, r, c = map(int, input().split())
    # 1. 블럭 배치
    h = locate(board_g, t, c)
    # 2. 점수 체크
    point, h = check_point(board_g, h)
    ans += point
    # 3. 블럭 이동
    if h: move_block(board_g, h, 1)
    # 4. 초과 블럭 확인
    h = check(board_g)
    # 5. 블럭 이동
    if h: move_block(board_g, h, 0)

    # 블럭, 좌표 변환
    nt, nr, nc = trans(t, r, c)
    # 1. 블럭 배치
    h = locate(board_b, nt, nc)
    # 2. 점수 체크
    point, h = check_point(board_b, h)
    ans += point
    # 3. 블럭 이동
    if h: move_block(board_b, h, 1)
    # 4. 초과 블럭 확인
    h = check(board_b)
    # 5. 블럭 이동
    if h: move_block(board_b, h, 0)

# 점수 출력
print(ans)
cnt = 0
for i in range(6):
    for j in range(4):
        if board_b[i][j]: cnt += 1
        if board_g[i][j]: cnt += 1
print(cnt)