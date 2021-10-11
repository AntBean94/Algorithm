# BOJ 11725 트리의 부모 찾기

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
tree = [i for i in range(N + 1)]
graph = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 순회하면서 부모 결정
vis = [0] * (N + 1)
Q = deque()
Q.append(1)
vis[1] = 1
while Q:
    i = Q.popleft()
    for j in graph[i]:
        if not vis[j]:
            Q.append(j)
            vis[j] = 1
            tree[j] = i
for i in tree[2:]:
    sys.stdout.writelines(f'{i}\n')