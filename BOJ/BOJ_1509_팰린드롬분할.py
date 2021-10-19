# BOJ 1509 팰린드롬 분할

'''
문자열의 최대길이 2500
N^2 알고리즘 통과 가능

팰린드롬 분할의 최소 개수 구하기

QWERTYTREWQWERT
Q, W, E, R, T, Y, TREWQWERT = 7개
q, w, e, r, tyt, r....
QWERTYTREWQ, W, E, R, T = 5개

1. 모든 구간 펠린드롬 기록
- 2차원 배열 활용
- N^2

2. 시작점부터 끝점까지 최단거리 측정
- BFS 또는 DP

'''
from collections import deque

char = input()
N = len(char)
# 모든 팰린드롬 확인
graph = [list() for _ in range(N)]
for i in range(N):
    l, r = i, i
    # 홀수 팰린드롬
    while l >= 0 and r < N:
        if char[l] == char[r]:
            graph[l].append(r)
            l -= 1
            r += 1
        else: break
    if i == N - 1: break
    l, r = i, i + 1
    # 짝수 팰린드롬
    while l >= 0 and r < N:
        if char[l] == char[r]:
            graph[l].append(r)
            l -= 1
            r += 1
        else: break

# bfs
def bfs(x):
    vis = [0] * N
    Q = deque()
    Q.append(x)
    vis[x] = 1
    while Q:
        x = Q.popleft()
        for y in graph[x][::-1]:
            if y + 1 == N:
                print(vis[x])
                exit()
            if not vis[y + 1]:
                vis[y + 1] = vis[x] + 1
                Q.append(y + 1)
    return
bfs(0)