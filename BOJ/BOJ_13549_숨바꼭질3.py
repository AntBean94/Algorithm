# BOJ 13549 숨바꼭질 3

'''
범위는 100,000

수빈이는 걷거나 순간이동 가능
걷는경우 1초 후에 X-1, X+1로 이동
순간이동 0초 후에 2*X로 이동

bfs
'''

from collections import deque
N, K = map(int, input().split())
nxt = lambda x: [2 * x, x - 1, x + 1]

def bfs(x):
    vis = [0] * 100001
    Q = deque()
    Q.append(x)
    vis[x] = 1
    # bfs
    while Q:
        x = Q.popleft()
        if x == K:
            return vis[x] - 1
        for i, y in enumerate(nxt(x)):
            if 0 <= y < 100001 and not vis[y]:
                if i == 0: vis[y] = vis[x]
                else: vis[y] = vis[x] + 1
                Q.append(y)

print(bfs(N))