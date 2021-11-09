# BOJ 9466 텀 프로젝트

'''
2 3 4 5 1 => 5명 한팀
2 3 4 4 1 => 1명 한팀


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

'''
6
2 3 4 5 6 2
output : 1

5
2 5 4 5 2
output : 3

6
1 3 4 3 2 6
output : 2

13
2 4 5 2 4 1 8 9 10 11 9 10 10
output : 8

10
2 5 7 1 6 8 8 3 5 10
output : 6

10
2 7 10 5 3 3 9 10 6 3
output : 8

6
2 1 1 2 6 3
output : 4
'''