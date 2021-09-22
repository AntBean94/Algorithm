# BOJ 17837 새로운 게임 2

'''
말이 4개 이상 쌓이는 순간 게임이 종료된다.

0. 흰색
이동 후 위에 쌓인다.

1. 빨간색
이동 후 순서 뒤바뀐채로 위에 쌓인다.

2. 파란색
반대 방향으로 한칸 이동

N = 12
K = 10

게임이 종료되는 턴의 번호 출력
1,000보다 크거나 게임이 종료되지 않는 경우에 -1 출력

접근 방법

해시 사용
{1: [y, x, 방향, 높이], 2: [] ...}

스택 사용
2차원 리스트 원소를 스택으로 활용

1. 턴 시작 (while문, 1000턴까지)

2. 해시에서 하나씩 뽑아 방향에 맞게 이동시킨다.
    2-1. 움직일 방향을 확인한다.
    2-2. 움직일 방향의 색에 따라 분기
    2-3. 흰색일 경우 스택의 리스트 0번 인덱스부터 이동시킨후 기존 스택 비운다.
    2-4. 빨간색일 경우 스택의 top부터 하나씩 뽑아 이동시킨다.
    2-5. 파란색일 경우 반대방향으로 이동한다.
    => 중간중간 쌓인말이 4개 이상 쌓이면 턴을 기록하고 게임 종료

'''
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
stack = [list([] for _ in range(N)) for _ in range(N)]
info = {}
for i in range(1, K+1):
    r, c, d = map(int, input().split())
    info[i] = [r-1, c-1, d, 0]
    stack[r-1][c-1].append(i)

dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]
ans = 0
turn = 1
# 1. 반복(1000턴)
while turn <= 1000:
    # 2. 말을 하나씩 이동 
    for key, value in info.items():
        y, x, d, h = value
        # 2-1. 움직일 방향의 색 확인
        ny, nx = y + dy[d], x + dx[d]
        color = -1
        # 색 확인(맵 밖으로 나가면 파란색과 동일)
        if 0 <= ny < N and 0 <= nx < N: color = board[ny][nx]
        else: color = 2

        # 2-2. 색에 따라 움직이기
        # 흰색
        if color == 0:
            cnt = len(stack[ny][nx])
            # 이동(위에있는 친구들 데리고 가기)
            for i in stack[y][x][h:]:
                stack[ny][nx].append(i)
                info[i][0], info[i][1], info[i][3] = ny, nx, cnt
                cnt += 1    
            # 위에있는 친구들 제거
            while stack[y][x][h:]:
                stack[y][x].pop()
        # 빨간색
        elif color == 1:
            cnt = len(stack[ny][nx])
            # 이동(맨 위에있는 친구부터 먼저 이동)
            l = len(stack[y][x])
            for _ in range(l - h):
                now = stack[y][x].pop()
                stack[ny][nx].append(now)
                info[now][0], info[now][1], info[now][3] = ny, nx, cnt
                cnt += 1
        # 파란색
        else:
            # 반대방향으로 이동(위에있는 친구들 데리고 가기)
            ny, nx = y - dy[d], x - dx[d]
            if d == 1 or d == 3: d += 1
            else: d -= 1
            value[2] = d
            # 반대방향이 파란색, 바깥이라면 이동 X
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] != 2:
                if board[ny][nx] == 0:
                    cnt = len(stack[ny][nx])
                    for i in stack[y][x][h:]:
                        stack[ny][nx].append(i)
                        info[i][0], info[i][1], info[i][3] = ny, nx, cnt
                        cnt += 1
                    while stack[y][x][h:]:
                        stack[y][x].pop()
                    if cnt >= 4:
                        ans = turn
                        break
                elif board[ny][nx] == 1:
                    cnt = len(stack[ny][nx])
                    l = len(stack[y][x])
                    for _ in range(l - h):
                        now = stack[y][x].pop()
                        stack[ny][nx].append(now)
                        info[now][0], info[now][1], info[now][3] = ny, nx, cnt
                        cnt += 1
            # 이동 후 높이 체크
            if cnt >= 4:
                ans = turn
                break
    # 턴 종료
    if ans: break
    else: turn += 1

if ans: print(ans)
else: print(-1)