# BOJ 20058 마법사 상어와 파이어스톰

'''
접근 방법

1. 단계 결정 후 회전
2. 얼음 체크
3. 마지막에 최대 얼음크기 측정, 얼음 총합 측정

결과
1. 남아있는 얼음의 합
2. 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
    => bfs

1,000 * 4,000 = 4,000,000 (완탐 가능)

회전 알고리즘
N: 사각형 변의 길이
y, x: 기준점에서 얼마나 떨어져있는지
r, c: 현재 점의 인덱스
r+y, c+x => c+y, N+x+1-r

'''

N, Q = map(int, input().split())
board = [[]] + [[0]+list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 회전 알고리즘
def cycle(board, y, x, n):
    # print(y, x)
    for i in range(1, n//2+1):
        for j in range(i, n-(i-1)):
            tmp = -1
            r, c = i, j
            for k in range(4):
                if tmp==-1:
                    tmp = board[c+y][n+x+1-r]
                    board[c+y][n+x+1-r] = board[r+y][c+x]
                else:
                    board[c+y][n+x+1-r], tmp = tmp, board[c+y][n+x+1-r]
                r, c = c, n - r + 1

for l in range(len(L)):
    # 1. 회전
    for i in range(0, 2**N, 2**L[l]):
        for j in range(0, 2**N, 2**L[l]):
            cycle(board, i, j, 2**L[l])
    # 2. 얼음 체크
    tmp = []
    for i in range(1, 2**N+1):
        for j in range(1, 2**N+1):
            cnt = 0
            for d in range(4):
                ny, nx = i + dy[d], j + dx[d]
                if 0 < ny < 2**N+1 and 0 < nx < 2**N+1:
                    if board[ny][nx]: cnt += 1
            if cnt < 3 and board[i][j] > 0: tmp.append([i, j])
    # 3. 얼음 감소
    for i, j in tmp:
        board[i][j] -= 1

# 남은 얼음의 합
ans1 = 0
for i in range(1, 2**N+1):
    for j in range(1, 2**N+1):
        ans1 += board[i][j]

def bfs(y, x):
    tmp = 0
    vis[y][x] = 1
    Q = []
    Q.append([y, x])
    while Q:
        y, x = Q.pop(0)
        tmp += 1
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 < ny < 2**N+1 and 0 < nx < 2**N+1:
                if board[ny][nx] and not vis[ny][nx]:
                    vis[ny][nx] = 1
                    Q.append([ny, nx])
    return tmp

ans2 = 0
# 최대 얼음 크기
vis = [[0] * (2**N+1) for _ in range(2**N+1)]
for i in range(1, 2**N+1):
    for j in range(1, 2**N+1):
        if not vis[i][j] and board[i][j]:
            result = bfs(i, j)
            if result > ans2:
                ans2 = result
print(ans1)
print(ans2)