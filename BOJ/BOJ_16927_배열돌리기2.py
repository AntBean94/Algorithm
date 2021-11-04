# BOJ 16927 배열 돌리기 2

'''
접근방법
배열을 테두리의 길이에 따라 그룹화 시킨뒤
그룹화된 좌표 배열을 순회하면서 새로운 배열에 값을 담는다. 

'''
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def make_arr(vis, k):
    tmp = []
    y, x, d = k, k, 0
    tmp.append([y, x])
    vis[y][x] = 1
    while d < 4:
        ny, nx = y + dy[d], x + dx[d]
        if i <= ny < N - i and i <= nx < M - i and not vis[ny][nx]:
            vis[ny][nx] = 1
            tmp.append([ny, nx])
            y, x = ny, nx
        else: d += 1
    return tmp

trans_arr = {}
vis = [[0] * M for _ in range(N)]
m = min(N, M) // 2
for i in range(m):
    key = 2 * (N + M - 4 * i - 2)
    trans_arr[key] = make_arr(vis, i)

new_arr = [[0] * M for _ in range(N)]
for key, value in trans_arr.items():
    r = R % key  # 이동할 거리
    for i in range(key):
        y, x = value[i]
        ny, nx = value[(i + r) % key]
        new_arr[ny][nx] = arr[y][x]

# 출력
for a in new_arr:
    print(*a)