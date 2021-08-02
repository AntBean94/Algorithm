# BOJ 14499 주사위 굴리기

# 정 육면체
'''
주사위 전개도
[1, 2, 3, 4, 5, 6]
동쪽: 1
서쪽: 2
북쪽: 3
남쪽: 4
[1, 2, 3, 4, 5, 6]
동쪽: 1 => 4, 2 => 2, 3 => 1, 4 => 6, 5 => 5, 6 => 3
서쪽: 1 => 3, 2 => 2, 3 => 6, 4 => 1, 5 => 5, 6 => 4
북쪽: 1 => 5, 2 => 1, 3 => 3, 4 => 4, 5 => 6, 6 => 2
남쪽: 1 => 2, 2 => 6, 3 => 3, 4 => 4, 5 => 1, 6 => 5

주사위 이동 동선
[
    [4, 2, 1, 6, 5, 3],
    [3, 2, 6, 1, 5, 4],
    [5, 1, 3, 4, 6, 2],
    [2, 6, 3, 4, 1, 5]
]
'''

import sys
input = sys.stdin.readline
N, M, Y, X, K = map(int, input().split())
maps = [list(map(int, input().split())) for i in range(N)]
command = list(map(int, input().split()))

turn = [
    [3, 1, 0, 5, 4, 2],
    [2, 1, 5, 0, 4, 3],
    [4, 0, 2, 3, 5, 1],
    [1, 5, 2, 3, 0, 4]
]
dice = [0] * 6
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]

def rolling_dice(dice, dir):
    dice[turn[dir][0]], dice[turn[dir][1]], dice[turn[dir][2]], dice[turn[dir][3]], dice[turn[dir][4]], dice[turn[dir][5]] = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

x, y = X, Y
for d in command:
    # 벗어나는지 체크
    if not(0 <= x + dx[d] < M and 0 <= y + dy[d] < N):
        continue
    x += dx[d]
    y += dy[d]
    rolling_dice(dice, d - 1)
    value = maps[y][x]
    if value == 0:
        maps[y][x] = dice[0]
    else:
        dice[0] = value
        maps[y][x] = 0
    print(dice[5])

    


