# BOJ 13913 숨바꼭질 4

'''
걷거나 순간이동
걸을때는 -1, +1
순간이동 *2

BFS?
'''
from collections import deque

N, K = map(int, input().split())

def move(x):
    result = set()
    a, b, c = x - 1, x + 1, x * 2
    if a >= 0: result.add(a)
    if b <= 100000: result.add(b)
    if c <= 100000: result.add(c)
    return result

def bfs(n, k):
    vis = [0] * 100001
    route = [0] * 100001
    Q = deque()
    Q.append(n)
    vis[n] = 1
    route[n] = n
    while Q:
        x = Q.popleft()
        if x == k: break
        for y in move(x):
            if not vis[y]:
                Q.append(y)
                vis[y] = 1
                route[y] = x
    result = [k]
    p = k
    while p != n:
        p = route[p]
        result.append(p)
    print(len(result)-1)
    print(*result[::-1])
    return

bfs(N, K)