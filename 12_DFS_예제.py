# DFS (깊이 우선 탐색) 예제

import sys

link = [[], [2, 3], [1, 3, 4, 5], [1, 2, 6, 7], [2, 5], [2, 4], [3, 7], [3, 6]]
visit = [0] * len(link)

def dfs(start):
    if visit[start]:
        return
    visit[start] = 1
    sys.stdout.writelines(str(start) + '\n')
    for branch in link[start]:
        dfs(branch)

dfs(1)