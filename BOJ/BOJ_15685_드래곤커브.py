# BOJ 15685 드래곤 커브

'''
N
x y d g
시작점, 방향, 세대

90도 변환 => 

0 -> 1
0, 1 -> 1, 2
0, 1, 2, 1 -> 1, 2, 3, 2

즉, 세대를 거듭하더라도 자기보다 1큰 방향으로만 바뀐다.



'''

N = int(input())

# 우, 상, 좌, 하
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

# 방향 정보
start = []
dir = [list() for _ in range(N)]
vis = [[0] * 101 for _ in range(101)]

# 드래곤 커브 그리기
for i in range(N):
    x, y, d, g = map(int, input().split())
    s = 0
    dir[i].append(d)
    while s < g:
        n = 2 ** s
        for j in dir[i][::-1]:
            dir[i].append((j + 1) % 4)
        s += 1
    vis[y][x] = 1
    for d in dir[i]:
        y += dy[d]
        x += dx[d]
        vis[y][x] = 1

# 박스 갯수 세기
ans = 0
for i in range(100):
    for j in range(100):
        if vis[i][j] and vis[i + 1][j] and vis[i][j + 1] and vis[i + 1][j + 1]:
            ans += 1
print(ans)