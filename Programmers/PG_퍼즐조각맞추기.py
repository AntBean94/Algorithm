'''
블록을 어떻게 처리?

50 * 50 = 2500

빈칸의 크기는 최대 6

블록의 방향을 기억?

블록의 크기별로 배열에 저장

기준점은 항상 (행, 열)이 작은 포인트

2500 / 1 = 2500개
빈칸을 감안하면 블럭은 최대 1250개 (1개짜리 블럭만 있는 경우)

2500 * 450 * 4(방향) * 3(블럭) = 약 1500만
2500 * 1200 = 약 3,000,000

몇 칸을 채울 수 있는지 return

빈칸과 블럭 비교는
블럭 좌표배열을 회전시키는 함수 만든다.
배열을 회전시키면서 좌표간의 거리 측정
좌상단부터 좌표간의 거리가 모두 같다면 같은 블럭
'''


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def check_lth(board, n, y, x):
    arr = []
    cnt = 0
    vis = [[0] * n for _ in range(n)]
    vis[y][x] = 1
    Q = []
    Q.append([y, x])
    while Q:
        y, x = Q.pop()
        cnt += 1
        arr.append([y, x])
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < n and 0 <= nx < n and not vis[ny][nx]:
                if not board[ny][nx]:
                    Q.append([ny, nx])
                    vis[ny][nx] = 1
    # 길이 기록
    for y, x in arr:
        board[y][x] = -cnt
    return

# 블럭 확인 함수
def check_block(table, vis, N, y, x):
    cnt = 0
    info = []
    Q = []
    Q.append([y, x])
    vis[y][x] = 1
    while Q:
        y, x = Q.pop()
        info.append([y, x])
        cnt += 1
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                if not vis[ny][nx] and table[ny][nx]:
                    vis[ny][nx] = vis[y][x] + 1
                    Q.append([ny, nx])
    return cnt, sorted(info)

# 배열 회전 함수
def cycle(arr, N):
    new_arr = []
    # 시계방향 90도 회전
    for y, x in arr:
        ny = x
        nx = N - y - 1
        new_arr.append([ny, nx])
    return new_arr

# 블럭 매칭 함수
def matching(board, block, vis, N, y, x):
    vis[y][x] = 1
    now = []
    Q = []
    Q.append([y, x])
    while Q:
        y, x = Q.pop()
        now.append([y, x])
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                if not vis[ny][nx] and board[ny][nx] < 0:
                    vis[ny][nx] = 1
                    Q.append([ny, nx])
    l = len(now)
    for d in range(4):
        # now배열 방향 전환 및 정렬
        if d != 0: now = cycle(now, N)
        now.sort()
        # block과 비교
        for key, value in block.items():
            dif_a, dif_b = 100000, 100000
            cnt = 1
            for i in range(l):
                cur_a = now[i][0] - value[i][0]
                cur_b = now[i][1] - value[i][1]
                # 초기값 설정
                if dif_a + dif_b > 100000:
                    dif_a = cur_a
                    dif_b = cur_b
                # 비교
                else:
                    if dif_a == cur_a and dif_b == cur_b: cnt += 1
                    else: break
            if cnt == l:
                del block[key]
                return l
    return 0

def solution(game_board, table):
    answer = 0
    N = len(game_board)
    # 빈칸 측정
    for i in range(N):
        for j in range(N):
            if not game_board[i][j]:
                check_lth(game_board, N, i, j)
    # 블럭 종류 확인
    block = {i:dict() for i in range(1, 7)}
    id = 0
    vis = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not table[i][j] or vis[i][j]: continue
            k, arr = check_block(table, vis, N, i, j)
            block[k][id] = arr
            id += 1
    # 배열을 순회하면서 블럭과 매칭
    vis = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            n = -game_board[i][j]
            if n < 1 or vis[i][j]: continue
            result = matching(game_board, block[n], vis, N, i, j)
            if result: answer += result
    # 결과 = 몇 칸을 채울 수 있는지 확인
    return answer

test_case = [
    [[[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]],
    [[[0,0,0],[1,1,0],[1,1,1]], [[1,1,1],[1,0,0],[0,0,0]]],
    [[[1, 0, 0], [0, 0, 1], [1, 0, 0]], [[0, 1, 0], [1, 1, 1], [1, 0, 1]]]
]
for tc in test_case:
    print(solution(tc[0], tc[1]))