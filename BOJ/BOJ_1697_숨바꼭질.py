# BOJ 1697 숨바꼭질

'''

5 6 7 8 16 17

5 10 9 18 17

bfs
'''

from collections import deque

N, K = map(int, input().split())
if N == K:
    print(0)
    exit()

dx = [-1, 1]

vis = [0] * 100001

def bfs(x):
    vis[x] = 1
    Q = deque()
    Q.append(x)
    while Q:
        x = Q.popleft()
        # 앞, 뒤 이동
        for d in range(2):
            nx = x + dx[d]
            if 0 <= nx < 100001 and not vis[nx]:
                vis[nx] = vis[x] + 1
                Q.append(nx)
                if nx == K:
                    print(vis[nx] - 1)
                    exit()
        # 순간 이동
        nx = 2 * x
        if 0 <= nx < 100001 and not vis[nx]:
            vis[nx] = vis[x] + 1
            Q.append(nx)
            if nx == K:
                print(vis[nx] - 1)
                exit()

bfs(N)