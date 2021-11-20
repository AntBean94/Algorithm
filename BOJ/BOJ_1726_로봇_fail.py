# BOJ 1726 로봇 fail

# 오답 코드
'''
bfs

큐에 넣을 때
[y, x, 방향]

이동이 가능한 방향은 자신의 반대방향을 제외한곳
같은 방향은 이동시 cnt가 1증가
다른 방향은 이동시 cnt가 2증가

목적지에서 코스트 별도로 계산

change = lambda x: [x, x-1, x+1]
방향 전환, 같은 방향
for nd in change(d):
    if nd == d:
        같은 방향
        이동 =>
        카운트 체크해서 1증가여부 확인
    else:
        다른 방향
        이동 =>
        2 증가한뒤 이동

(5, 6) (6, 5) 
'''

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
factory = [list(map(int, input().split())) for _ in range(N)]
departure = list(map(int, input().split()))
arrival = list(map(int, input().split()))
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
change = lambda x: [x, x + 1, x - 1, x + 2]
trans = [0, 1, 3, 2, 0]

def bfs(start, goal):
    y, x, d = start
    y, x, d = y - 1, x - 1, trans[d]
    Q = deque()
    vis = [[0] * M for _ in range(N)]
    ans = []
    if y == goal[0] - 1 and x == goal[1] - 1:
        ans.append([d, 1])
    else:
        Q.append([y, x, d])
        vis[y][x] = 1
    while Q:
        y, x, d = Q.popleft()
        for nd in change(d):
            # 같은 방향 이동
            if nd == d:
                # print(nd)
                for i in range(1, 4):
                    ny, nx = y + dy[nd] * i, x + dx[nd] * i
                    if 0 <= ny < N and 0 <= nx < M:
                        if factory[ny][nx]: break
                        nv = vis[y][x] + 1
                        if (not vis[ny][nx] or nv < vis[ny][nx]):
                            vis[ny][nx] = nv
                            Q.append([ny, nx, nd])
                        if ny == goal[0] - 1 and nx == goal[1] - 1:
                            ans.append([nd, nv])
            # 다른 방향 이동
            else:
                nd = nd % 4
                for i in range(1, 4):
                    ny, nx = y + dy[nd] * i, x + dx[nd] * i
                    if 0 <= ny < N and 0 <= nx < M:
                        if factory[ny][nx]: break
                        nv = vis[y][x] + 3 if abs(d - nd) == 2 else vis[y][x] + 2
                        if (not vis[ny][nx] or nv < vis[ny][nx]):
                            vis[ny][nx] = nv
                            Q.append([ny, nx, nd])
                        if ny == goal[0] - 1 and nx == goal[1] - 1:
                            # print('angs', [nd, nv])
                            ans.append([nd, nv])
    # 방향 계산 이후 결과값 반환
    min_val = 100000000
    gd = trans[goal[2]]
    for dir, dis in ans:
        result = dis - 1
        tmp = abs(dir - gd)
        # print(tmp)
        if tmp == 2: result += 2
        elif tmp == 1 or tmp == 3: result += 1
        # print(dis-1, tmp)
        if result < min_val: min_val = result

    # for v in vis:
    #     print(v)
    return min_val
print(bfs(departure, arrival))