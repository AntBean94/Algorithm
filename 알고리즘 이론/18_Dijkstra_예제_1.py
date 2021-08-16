# 18강 다익스트라 알고리즘 (Dijkstra Algorithm) 예제 (1)

# 선형 탐색 알고리즘 - O(N^2)

n = 6
INF = 1000000000
a = [[0, 2, 5, 1, INF, INF],
    [2, 0, 3, 2, INF, INF],
    [5, 3, 0, 3, 1, 5],
    [1, 2, 3, 0, 1, INF],
    [INF, INF, 1, 1, 0, 2],
    [INF, INF, 5, INF, 2, 0]]

v = [0] * n
d = [0] * n

# 최단거리 반환 함수
def getSmallIndex():
    m = INF
    index = 0
    for i in range(n):
        if d[i] < m and not v[i]:
            m = d[i]
            index = i
    return index

# 다익스트라 알고리즘 수행 함수
def dijkstra(start):
    # 거리 초기화
    for i in range(n):
        d[i] = a[start][i]
    v[start] = 1
    # 최단거리 찾아가며 거리 수정
    for i in range(n - 1):
        cur = getSmallIndex()
        v[cur] = 1
        for j in range(n):
            if not v[j] and d[cur] + a[cur][j] < d[j]:
                d[j] = d[cur] + a[cur][j]

dijkstra(0)
print(*d)
            

