# BOJ 2887 행성 터널

'''
3차원
100000

정렬을 세번하면
각각
1. x좌표 작은순 정렬
2. y좌표 작은순 정렬
3. z좌표 작은순 정렬
세개의 배열을 만들 수 있다.

=> 즉 x좌표 작은순, y좌표 작은순, z좌표 작은순 정렬시
   양 옆의 좌표만 확인하면된다.

양옆 간선의 최솟값
'''
import sys
input = sys.stdin.readline

G = [list() for i in range(3)]

N = int(input())
for i in range(1, N + 1):
    x, y, z = map(int, input().split())
    G[0].append([i, x])
    G[1].append([i, y])
    G[2].append([i, z])

for i in range(3):
    G[i].sort(key=lambda x: x[1])

R = []
for i in range(3):
    for j in range(N - 1):
        R.append([G[i][j][0], G[i][j + 1][0], abs(G[i][j][1] - G[i][j+1][1])])

R.sort(key=lambda x: x[2])

def get_parent(graph, x):
    if x == graph[x]: return x
    graph[x] = get_parent(graph, graph[x])
    return graph[x]

def union_parent(graph, x, y):
    x = get_parent(graph, x)
    y = get_parent(graph, y)
    if x <= y: graph[y] = x
    else: graph[x] = y

def find_parent(graph, x, y):
    x = get_parent(graph, x)
    y = get_parent(graph, y)
    if x == y: return True
    else: return False

graph = [i for i in range(N + 1)]
ans, cnt = 0, 0
for a, b, g in R:
    if not find_parent(graph, a, b):
        union_parent(graph, a, b)
        ans += g
        cnt += 1
    if cnt == N - 1: break
print(ans)