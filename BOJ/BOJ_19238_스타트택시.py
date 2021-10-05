# BOJ 19238 스타트 택시

'''
1. 가장 가까운 승객찾기
- bfs
- 거리가 같은 승객이 여럿이면, 행, 열번호가 작은 승객을 고른다.
- 연료 가능 여부 확인

2. 목적지 거리계산하기
- bfs
- 연료 가능여부 확인

3. 연료 충전량
- (승객찾는데 걸린 거리 + 목적지 거리) * 2

결과
모든 손님을 이동시키고 충전한 후 남은 연료의 양을 출력
모든 손님을 이동시킬 수 없는 경우 -1출력

'''

N, M, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
sy, sx = map(int, input().split())
sy, sx = sy - 1, sx - 1
goal_info = {}
for i in range(2, M + 2):
    a, b, c, d = map(int, input().split())
    board[a-1][b-1] = i
    goal_info[i] = [c-1, d-1]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 가까운 승객찾는 함수
def find_user(board, y, x):
    vis = [[0] * N for _ in range(N)]
    min_dist = 100000
    user_arr = []
    Q = []
    Q.append([y, x])
    vis[y][x] = 1
    while Q:
        y, x = Q.pop(0)
        # 손님이면서 최단거리가 같은 경우
        if vis[y][x] <= min_dist:
            if 1 < board[y][x] < 1000:
                user_arr.append([y, x])
                min_dist = vis[y][x]
        else: break
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                # 1이 아니면서 방문기록이 없는 경우 경로에 추가
                if board[ny][nx] != 1 and not vis[ny][nx]:
                    vis[ny][nx] = vis[y][x] + 1
                    Q.append([ny, nx])
    # 가능한 목록중에 최단거리 손님 뽑아내기
    user_arr.sort()
    # 경로가 막혀있는경우
    if user_arr: uy, ux = user_arr[0]
    else:
        print(-1)
        exit()
    user = board[uy][ux]
    # 방문한 노드는 board에서 정보 지우기
    board[uy][ux] = 0
    return user, uy, ux, min_dist - 1


# 목적지 거리 계산기
def cal_goal(board, user, y, x, gy, gx):
    user += 1000
    vis = [[0] * N for _ in range(N)]
    Q = []
    Q.append([y, x])
    vis[y][x] = 1
    while Q:
        y, x = Q.pop(0)
        if y == gy and x == gx:
            return vis[y][x] - 1
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                if board[ny][nx] != 1 and not vis[ny][nx]:
                    vis[ny][nx] = vis[y][x] + 1
                    Q.append([ny, nx])
    print(-1)
    exit()

# M번 반복
for i in range(M):
    # 최단 거리 승객과 위치, 거리 리턴
    user, y, x, dist_a = find_user(board, sy, sx)
    sy, sx = y, x
    # 연료 체크
    if fuel >= dist_a: fuel -= dist_a
    else:
        print(-1)
        exit()
    # 목적지까지의 최단거리 리턴
    gy, gx = goal_info[user]
    dist_b = cal_goal(board, user, y, x, gy, gx)
    # 연료 체크
    if fuel >= dist_b: fuel -= dist_b
    else:
        print(-1)
        exit()
    # 연료 충전
    fuel += dist_b * 2
    # 좌표 이동
    sy, sx = gy, gx
print(fuel)