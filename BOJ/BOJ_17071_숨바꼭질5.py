# BOJ 17071 숨바꼭질 5

'''
동생의 위치 = 등차수열의 합 = K + t(t + 1)/2

1. 언니의 위치는 최초 방문 이후 + 짝수시간에 방문 가능(+1, -1)
2. x시간대의 최초 방문 시간보다 y시간의 다음 방문시간(홀, 짝 대비)에 방문했을 때
더 빠를수 있음. 즉, 방문 기록을 홀, 짝 각각 최소기록을 구해놓아야 함
'''

from collections import deque

INF = 100000000
N, K = map(int, input().split())
vis = [[0] * 2 for _ in range(500001)]
# print(vis[:10])

cal = lambda x: [x - 1, x + 1, 2 * x]

def bfs(start):
    vis[start][0] = 1
    Q = deque()
    Q.append([start, 0])
    while Q:
        x, check = Q.popleft()
        for y in cal(x):
            if 0 <= y <= 500000:
                # 홀수인경우 y는 짝수
                if vis[x][check] % 2 and not vis[y][1]:
                    vis[y][1] = vis[x][check] + 1
                    Q.append([y, 1])
                elif not vis[x][check] % 2 and not vis[y][0]:
                    vis[y][0] = vis[x][check] + 1
                    Q.append([y, 0])

bfs(N)
ans = INF
for time in range(1010):
    loc = K + time * (time + 1) // 2
    if loc > 500000: break
    c = time % 2
    big = vis[loc][c]
    if not big or time < big - 1: continue
    if time < ans:
        ans = time
        print(loc)
if ans == INF: print(-1)
else: print(ans)