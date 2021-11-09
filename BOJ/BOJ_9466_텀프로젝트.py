# BOJ 9466 텀 프로젝트

'''
2 3 4 5 1 => 5명 한팀
2 3 4 4 1 => 1명 한팀

접근 방법
1. 각각의 팀과 순서를 기록
2. 팀이 일치하면서 순서가 다르면 그 순서의 차이만큼 카운트 기록
'''

import sys
input = sys.stdin.readline

def dfs(graph, vis, start, t):
    vis[start] = [t, 1]
    cnt = 1
    stack = [start]
    while stack:
        x = stack.pop()
        y = graph[x]
        cnt += 1
        if not vis[y][0]:
            vis[y] = [t, cnt]
            stack.append(y)
        elif vis[y][0] == t:
            return cnt - vis[y][1]
    return 0

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    vis = {i: [0, 0] for i in range(1, N + 1)}
    ans = N
    turn = 1
    for i in range(1, N + 1):
        if not vis[i][0]:
            result = dfs(arr, vis, i, turn)
            ans -= result
            turn += 1
    print(ans)