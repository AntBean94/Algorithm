# 19강 플로이드 와샬 (Floyd Warshall) 예제

INF = 100000000

# 거리정보 초기화
a = [
    [0, 5, INF, 8],
    [7, 0, 9, INF],
    [2, INF, 0, 4],
    [INF, INF, 3, 0]
]
N = len(a)

def floydWarshall():
    # 최단거리 초기화
    d = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            d[i][j] = a[i][j]
    # k를 거치는
    for k in range(N):
        # 출발지점(i)과 도착지점(j)
        for i in range(N):
            for j in range(N):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]

    return d

ans = floydWarshall()

for i in range(N):
    print(*ans[i], end="\n")