# BOJ 21611 마법사 상어와 블리자드

'''
상, 하, 좌, 우
1, 2, 3, 4

1. 얼음파편 던지기
=> 방향, 거리

2. 구슬은 상어를 기준으로 가운데로 모인다.

3. 구슬 폭발
- 같은 번호가 4개이상 연속되는 구슬이 폭발
- 다시 구슬 이동
- 이동 후 연속되는 구슬 다시 폭발 반복(연속 구슬이 없을 때 까지)

4. 구슬 변화
- 각 구슬 그룹을 A, B로 바꿔서 다시 넣는다.
- A: 구슬 그룹의 구슬 갯수
- B: 구슬을 이루는 번호
- 칸보다 많은 경우 버림


결과 = 1x(폭발한 1번구슬갯수) + 2x(2번) + 3x(3번)

접근 방법
1차원 배열 활용

방향별 인덱스
- 3방향(좌): 1, 10, 27...
- 2방향(하): 3, 14, 33...
- 4방향(우): 5, 18, 39...
- 1방향(상): 7, 22, 45...


=========== 주의(첫 번째 오답 원인) ===========

trans 함수에서
if num: 조건을 주지 않으면
배열에 아무것도 없는경우 배열복사가 일어난다.
0 => 1
1 => 1,1
:
:
'''

N, M = map(int, input().split())
point = [0] * 4

# 방향 인덱스
d_idx = [[] for _ in range(5)]
change = [3, 2, 4, 1]
n, d = 1, 2
while n < N ** 2:
    for i in range(4):
        d_idx[change[i]].append(n)
        n += d
    d += 1
    n += 1
    d += 1

# 1차원 배열로 전환
tmp = []
for i in range(N):
    tmp.append(list(map(int, input().split())))
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
d = 0
vis = [[0] * N for _ in range(N)]
board = []
y, x = N // 2, N // 2
while 0 <= x < N:
    board.append(tmp[y][x])
    vis[y][x] = 1
    # 방향 전환 또는 이동
    if y == N // 2 and x == N // 2:
        y, x = y + dy[d], x + dx[d]
        continue
    nd = (d + 1) % 4
    ny, nx = y + dy[nd], x + dx[nd]
    if not vis[ny][nx]:
        y, x, d = ny, nx, nd
    else:
        y, x = y + dy[d], x + dx[d]
board[0] = -1

# 구슬 이동 함수
def moving(board):
    stack = []
    for i in range(N ** 2):
        n = board[i]
        if n:
            stack.append(n)
        board[i] = 0
    for i in range(len(stack)):
        board[i] = stack[i]


# 구슬 폭발 함수
def bomb(board):
    result = [0] * 4
    stack = [0]
    cnt = 1
    for i in range(N ** 2):
        if not board[i]: break
        if board[i] != board[stack[-1]]:
            # 다르다면
            if cnt >= 4:
                result[board[stack[0]]] += cnt
                for s in stack:
                    board[s] = 0
            stack = [i]
            cnt = 1
        else:
            cnt += 1
            stack.append(i)
    if cnt >= 4:
        result[board[stack[0]]] += cnt
        for s in stack:
            board[s] = 0
    if sum(result): return result
    else: return False


def trans(board):
    stack = [-1]
    num = 0
    cnt = 1
    for i in board:
        if not i: break
        if i == -1: continue
        # 이외의 숫자에 대해 실행
        if i == num:
            cnt += 1
        else:
            if num:
                stack.append(cnt)
                stack.append(num)
            num = i
            cnt = 1
    if num:
        stack.append(cnt)
        stack.append(num)

    # 배열에 다시 넣기
    for i in range(N ** 2):
        board[i] = 0
        if i >= len(stack): continue
        board[i] = stack[i]
    

# 얼음 파편 던지기
turn = []
for i in range(M):
    turn.append(list(map(int, input().split())))

for d, s in turn:
    # 얼음 파편 던져서 구슬 깨뜨리기
    for i in d_idx[d][:s]:
        board[i] = 0
    # 구슬 이동
    moving(board)

    # 구슬 폭발
    while True:
        t_point = bomb(board)
        if t_point: 
            moving(board)
            for i in range(4):
                point[i] += t_point[i]
        else: break

    # 구슬 변화
    trans(board)

ans = 0
for i in range(1, 4):
    ans += i * point[i]
print(ans)