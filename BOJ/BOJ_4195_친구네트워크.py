# BOJ 4195 친구 네트워크

# 유니온 파인드
# 해시
import sys

def getParent(parent, x):
    if parent[x] == x: return x
    parent[x] = getParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a < b: 
        parent[b] = a
        group[a] += group[b]
    elif b < a: 
        parent[a] = b
        group[b] += group[a]

T = int(input())
for tc in range(T):
    bet = {}
    parent = [i for i in range(1000001)]
    group = [1] * 1000001
    num = 1
    N = int(input())
    for i in range(N):
        a, b = map(str, sys.stdin.readline().rstrip().split())
        if a not in bet:
            bet[a] = num
            num += 1
        if b not in bet:
            bet[b] = num
            num += 1
        # print(bet, bet[a], bet[b])
        unionParent(parent, bet[a], bet[b])
        # print('parent', parent[:10])
        # print('group', group[:10])
        print(group[getParent(parent, bet[a])])

        

