# BOJ 16946 벽 부수고 이동하기 4

'''
1. 매번 구역의 넓이를 계산하는건 비효율적
2. 각 구역값을 미리 구해두고 배열에 채운다.
3. 1을 없애고 주변 값 + 1이 정답 배열
'''
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[0] * M for _ in range(N)]
ID = [[0] * M for _ in range(N)]
for i in range(N):
    line = input().rstrip()
    for j in range(M):
        if line[j] == '1': G[i][j] = -1
        else: G[i][j] = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 그래프 넓이 채우기
def bfs(y, x, id):
    Q = deque()
    Q.append([y, x])
    vis[y][x] = 1
    stack = [[y, x]]
    while Q:
        y, x = Q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < M:
                if not vis[ny][nx] and not G[ny][nx]:
                    vis[ny][nx] = 1
                    Q.append([ny, nx])
                    stack.append([ny, nx])
    # 값 할당
    l = len(stack)
    for y, x in stack:
        G[y][x] = l
        ID[y][x] = id
    return

# bfs로 각 구역 넓이 구하기
vis = [[0] * M for _ in range(N)]
id = 1
for i in range(N):
    for j in range(M):
        if not vis[i][j] and not G[i][j]:
            bfs(i, j, id)
            id += 1

ans = ""
# 순회하며 정답 채우기
for i in range(N):
    for j in range(M):
        if G[i][j] == -1:
            result = 1
            check = set()
            for d in range(4):
                ny, nx = i + dy[d], j + dx[d]
                if 0 <= ny < N and 0 <= nx < M:
                    if G[ny][nx] > 0 and ID[ny][nx] not in check:
                        result += G[ny][nx]
                        check.add(ID[ny][nx])
            ans += f'{result % 10}'
        else:
            ans += '0'
    ans += '\n'
print(ans)