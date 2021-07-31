# BOJ 1976 여행 가자

# 유니온 파인드 알고리즘 활용
import sys

def getParent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = getParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a != b:
        if a < b: parent[b] = a
        else: parent[a] = b

def findParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a != b: return False
    else: return True

N = int(input())
M = int(input())

parent = [i for i in range(N + 1)]

for i in range(N):
    link = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(i+1, N):
        if link[j]: # 연결되어 있다면
            unionParent(parent, i + 1, j + 1)

road = list(map(int, input().split()))
ans = "YES"
for i in range(M-1):
    if not findParent(parent, road[i], road[i+1]):
        ans = "NO"
        break
print(ans)
