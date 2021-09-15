# BOJ 2580 스도쿠

'''
조건 만족 여부를 해시로 체크하기
'''

import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
info = [list(set() for _ in range(9)) for _ in range(3)]

Q = []
idx = 0
for i in range(9):
    for j in range(9):
        if not board[i][j]:
            Q.append([idx, i, j])
            idx += 1
        # 숫자인 경우
        else:
            info[0][i].add(board[i][j])
            info[1][j].add(board[i][j])
            loc = (i // 3) * 3 + (j // 3)
            info[2][loc].add(board[i][j])

# 가능한 숫자 탐색
N = len(Q)
pos = [list() for _ in range(N)]
full_set = set([i for i in range(1, 10)])
for idx, y, x in Q:
    loc = (y // 3) * 3 + (x // 3)
    tmp = (full_set - info[0][y]) & (full_set - info[1][x]) & (full_set - info[2][loc])
    pos[idx] = list(tmp)

def back_t(board, k):
    if k == N:
        for b in board:
            print(*b)
        exit()
    
    for i in pos[k]:
        idx, y, x = Q[k]
        loc = (y // 3) * 3 + (x // 3)
        # 보드에 들어갈 수 있는지 체크(info 활용)
        if i in info[0][y] or i in info[1][x] or i in info[2][loc]: continue
        # 각 집합에 i를 넣는다. 
        info[0][y].add(i)
        info[1][x].add(i)
        info[2][loc].add(i)
        # 보드에 값을 넣는다.
        board[y][x] = i
        # 재귀호출
        back_t(board, k + 1)
        # 보드에 값 제거
        board[y][x] = 0
        # 각 집합에서 i 를 제거한다.
        info[0][y].discard(i)
        info[1][x].discard(i)
        info[2][loc].discard(i)
    
back_t(board, 0)