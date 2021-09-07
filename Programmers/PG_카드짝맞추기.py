# Programmers 카드 짝 맞추기

''' 접근 방법

카드를 선택하는 경우의 수: 6! = 720

같은 카드 순서를 결정하는 경우의 수: 2 ^ 6 = 64

거리를 측정하는 bfs

1. 탐색할 카드의 순서를 결정한다.(순열)
2. 각 카드별 위치 중 먼저 탐색할 카드의 위치를 결정
3. bfs로 최단거리를 측정한다.

'''

import itertools

def solution(board, r, c):
    # for b in board:
    #     print(b)
    # print()
    answer = []
    # 1. 카드의 위치와 갯수 탐색
    loc = {}
    n = []
    for i in range(4):
        for j in range(4):
            card = board[i][j]
            if card:
                if card in loc: loc[card].append([i, j])
                else: loc[card] = [[i, j]]
                if card not in n: n.append(card)

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    opt = [[0, 1], [1, 0]]
    # 최단거리 측정
    def bfs(vis, y, x):
        vis[y][x] = 1
        q = []
        q.append([y, x, -1])
        while q:
            y, x, p = q.pop(0)
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < 4 and 0 <= nx < 4:
                    # 거리 체크
                    # 방향이 같은 경우 ans 번호가 없는 경우
                    if d == p and not board[y][x]: cost = vis[y][x]
                    # 그 외의 경우 모두 1증가
                    else: cost = vis[y][x] + 1
                    # 거리가 더 가까울경우에만 초기화
                    if vis[ny][nx] == 0 or cost <= vis[ny][nx]:
                        vis[ny][nx] = cost
                        q.append([ny, nx, d])

    # 순서대로 탐색하는 재귀 함수
    def solver(seq, k, y, x, dist, answer):
        ny, nx = y, x
        # print(k, dist)
        # 탈출 조건
        if k == len(seq):
            # if dist == 9:
            #     print('and', seq)
            # for b in board:
            #     print(b)
            # print()
            # if seq == (2, 3, 1):
            #     print(dist)
            if dist == 15:
                print(seq)
            answer.append(dist)
            return
        # print(k, '---------------')
        # 카드 순서별로 탐색
        card = seq[k]
        # 같은 카드간의 순서 결정
        for i in range(2):
            cnt = 0
            for j in opt[i]:
                vis = [[0] * 4 for _ in range(4)]
                bfs(vis, ny, nx)

                # if k == 0:
                #     for v in vis:
                #         print(v)
                #     print()
                ny, nx = loc[card][j][0], loc[card][j][1]
                board[ny][nx] = 0
                cnt += vis[ny][nx] - 1
                # if seq == (2, 3, 1):
                #     print(ny, nx)
                #     print(cnt)
                #     for v in vis:
                #         print(v)
                #     print()
                # print(vis[y][x])
                # print(cnt)
            # 다음 카드 탐색
            solver(seq, k+1, ny, nx, dist + cnt, answer)

            # 카드 탐색 끝났다면 좌표 및 카드 복구
            ny, nx = y, x
            board[loc[card][0][0]][loc[card][0][1]] = card
            board[loc[card][1][0]][loc[card][1][1]] = card

    # print()
    # 2. 탐색할 카드의 순서를 결정
    for case in itertools.permutations(n, len(n)):
        # print(case)
        solver(case, 0, r, c, 0, answer)
    answer = min(answer) + len(n) * 2
    # answer = min(answer)
    return answer


test_case = [
    [[[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0],
    [[[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1],
    # [[[1, 2, 0, 2], [3, 0, 4, 5], [5, 0, 1, 6], [3, 4, 0, 6]], 1, 1]
    [[[1, 2, 2, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 0, 1],
    [[[1, 2, 1, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 0, 1],
    [[[1, 0, 0, 3], [0, 2, 0, 0], [0, 0, 2, 0], [3, 0, 0, 1]], 2, 0],
    [[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]], 3, 1]
]
for tc in test_case:
    print(solution(tc[0], tc[1], tc[2]))