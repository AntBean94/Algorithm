# BOJ 9019 DSLR

'''
1234

3412

DSLR에 따라 수정 BFS
각 명령어는 큐에 함께 저장
수정한 값 방문체크(집합 활용)

(수정)
경로 문자열 저장시 시간초과
'''

from collections import deque

def trans(x:int):
    x = str(x)
    l = len(x)
    x = '0' * (4-l) + x
    return x

def bfs(a, b):
    vis = [0] * 10000
    vis[a] = a
    a = trans(a)
    b = trans(b)
    Q = deque()
    Q.append(a)
    while Q:
        x = Q.popleft()
        if x == b:
            break
        for i in range(4):
            # D
            if i == 0:
                y = trans((int(x) * 2) % 10000) 
                cmd = 'D'
            elif i == 1:
                y = trans((int(x) - 1) % 10000)
                cmd = 'S'
            elif i == 2:
                y = x[1:] + x[0]
                cmd = 'L'
            else:
                y = x[3] + x[:3]
                cmd = 'R'
            y_int = int(y)
            if not vis[y_int]:
                vis[y_int] = (cmd, x)
                Q.append(y)
    # vis 배열 역추적
    result = ""
    tmp = b
    while tmp != a:
        tmp = int(tmp)
        result += vis[tmp][0]
        tmp = vis[tmp][1]

    return result[::-1]

T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))