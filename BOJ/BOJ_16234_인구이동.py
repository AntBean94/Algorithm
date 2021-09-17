# BOJ 16234 인구 이동

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(board, y, x):
    vis[y][x] = 1
    stack = []
    total = 0
    Q = []
    Q.append([y, x, board[y][x]])
    while Q:
        y, x, po = Q.pop()
        total += po
        stack.append([y, x])
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                npo = board[ny][nx]
                if not vis[ny][nx] and L <= abs(po - npo) <= R:
                    Q.append([ny, nx, npo])
                    vis[ny][nx] = 1 
    if len(stack) == 1: return False
    else:
        mid = int(total / len(stack))
        for y, x in stack:
            board[y][x] = mid
        return True

# 1. 반복문
ans = 0
check = True
while check:
    check = False
    # 3. 방문 기록
    vis = [[0] * N for _ in range(N)]
    
    # 4. 그래프 반복
    for i in range(N):
        for j in range(N):
            if not vis[i][j]:
                if bfs(board, i, j): check = True
    if check: ans += 1
print(ans)