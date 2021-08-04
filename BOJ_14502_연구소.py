# BOJ 14502 연구소

'''
최악의 경우: 8*8 벽이 없고 바이러스 1개인 경우
약 40,000개의 조합이 발생
40,000 * 60 = 약 240만

'''

import sys
import copy
import itertools
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

# 백트래킹 조건(나중)
# 2의 갯수를 세며 최대 2의 갯수보다 작으면

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# bfs 함수
def bfs(start, maps):
    Q = []
    virus_num = 0
    for s in start:
        Q.append(s)
    while Q:
        t = Q.pop()
        # print(t)
        # print(Q)
        y, x = t[0], t[1]
        # print(maps)
        for d in range(4):
            # print(d)
            n_y = y + dy[d]
            n_x = x + dx[d]
            if 0 <= n_y < N and 0 <= n_x < M:
                if not maps[n_y][n_x]:
                    maps[n_y][n_x] = 2
                    Q.append([n_y, n_x])
                    virus_num += 1
    return virus_num
    

# 1. 0, 2 위치 저장
zero_loc = []
virus_loc = []
for i in range(N):
    for j in range(M):
        val = maps[i][j]
        if val == 0:
            zero_loc.append([i, j])
        elif val == 2:
            virus_loc.append([i, j])

min_virus = 100000000
# 2. 0 위치들로 조합 뽑아내기
for locs in itertools.combinations(zero_loc, 3):
    # 딥카피로 배열 복사
    new_map = copy.deepcopy(maps)
    # 2-1. 선택된 0 위치를 1로 바꾸기
    for i in locs:
        new_map[i[0]][i[1]] = 1
    # 2-2. bfs 돌리기
    virus_number = bfs(virus_loc, new_map)
    # 2의 갯수가 최소일 때
    if virus_number < min_virus:
        min_virus = virus_number

print(len(zero_loc) - min_virus - 3)