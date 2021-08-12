# BOJ 1516 게임 개발

'''로직
시간기록을 어떻게 할까?
=> DP

1-2-5
3-4/

1->2: 3
3->4: 2
2->5: 2
4->5: 1

0 3 0 2 5

큰 값으로 시간표 갱신
dp 테이블 출력
'''

from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
graph = [list() for _ in range(N + 1)]
indegree = [0] * (N + 1)
time = [0] * (N + 1)
dp_table = [0] * (N + 1)
for i in range(1, N+1):
    line = list(map(int, input().split()))
    time[i] = line[0]
    for j in line[1:-1]:
        graph[j].append(i)
        indegree[i] += 1
Q = deque()
# 진입차수 계산
for i in range(1, N+1):
    if indegree[i] == 0:
        Q.append(i)
        dp_table[i] = time[i]
# 반복문 
while Q:
    x = Q.popleft()
    for y in graph[x]:
        if indegree[y]:
            indegree[y] -= 1
            if dp_table[x] + time[y] > dp_table[y]:
                dp_table[y] = dp_table[x] + time[y]
            if indegree[y] == 0:
                Q.append(y)
# 출력
for d in dp_table[1:]:
    print(d)