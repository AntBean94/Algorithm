# BFS (너비 우선 탐색) 예제

from collections import deque
import sys

link = [[], [2, 3], [1, 3, 4, 5], [1, 2, 6, 7], [2, 5], [2, 4], [3, 7], [3, 6]]
visit = [0] * len(link)

def bfs(start):
    Q = deque()
    Q.append(start)
    visit[start] = True

    while Q:
        now = Q.popleft()
        sys.stdout.writelines(str(now) + '\n')
        for branch in link[now]:
            if not visit[branch]:
                visit[branch] = 1
                Q.append(branch)

bfs(1)