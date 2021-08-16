# BOJ 1389 케빈 베이컨의 6단계 법칙

# bfs 너비 우선탐색, 거리측정, visited 리스트 더하기

def bfs(s):
    visit[s] = 1
    Q = []
    Q.append(s)
    while Q:
        t = Q.pop(0)
        for v in link[t]:
            if visit[v]==0:
                visit[v] = visit[t] + 1
                Q.append(v)

N, M = map(int, input().split())
link = [list() for _ in range(N+1)]
for m in range(M):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

total = 100000000
ans = 0
for i in range(1, N+1):
    visit = [0] * (N+1)
    bfs(i)
    if sum(visit) < total:
        total = sum(visit)
        ans = i

print(ans)