# BOJ 2162 선분 그룹

'''
그룹 포함 여부 - union-find
선분 교차 여부 - 교차 알고리즘

다른 선분과 비교하기 위한 자료구조는?
다른 모든 선분과 전부 비교하게 되면
3000 * 3000 = 9,000,000

CCW
판별식 D = (x2 - x1)(y3 - y1) - (x3 - x1)(y2 - y1)

1. 데이터 입력
2. 모든 데이터 순회(2중 for문)
3. 교차여부 판별(CCW)
4. 교차한다면 union-find
5. 그룹갯수, 최대그룹크기 출력
'''

import sys
input = sys.stdin.readline

N = int(input())
lines = []
for i in range(N):
    a, b, c, d = map(int, input().split())
    lines.append([a, b, c, d])

# union-find
def get_parent(x, graph):
    if x == graph[x]: return x
    graph[x] = get_parent(graph[x], graph)
    return graph[x]

def union_parent(x, y, graph):
    x = get_parent(x, graph)
    y = get_parent(y, graph)
    if x < y: graph[y] = x
    else: graph[x] = y

# ccw
def ccw(line, x3, y3):
    x1, y1, x2, y2 = line
    D = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    return D

# 선분 교차 판별
def cross_line(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    # ccw 1
    result1 = ccw(line1, x3, y3) * ccw(line1, x4, y4)
    # ccw 2
    result2 = ccw(line2, x1, y1) * ccw(line2, x2, y2)
    # 결과 반환
    if result1 == 0 and result2 == 0:
        # 예외(수평선 - 상대위치 비교)
        if x1 - x2 == 0: x1, x2, x3, x4 = y1, y2, y3, y4
        if x2 < x1: x1, x2 = x2, x1
        if x4 < x3: x3, x4 = x4, x3
        if x2 < x3 or x1 > x4: return False
        else: return True
    elif result1 <= 0 and result2 <= 0: return True
    else: return False

group = [i for i in range(N)]
# 순회
for i in range(N):
    line1 = lines[i]
    for j in range(i + 1, N):
        line2 = lines[j]
        # 선분 교차 판별
        if not cross_line(line1, line2): continue
        # 선분이 교차하는 경우 union-find
        union_parent(i, j, group)

# 그룹갯수, 최대그룹크기
ans = {}
for i in range(N):
    p = get_parent(i, group)
    if p in ans: ans[p] += 1
    else: ans[p] = 1
print(len(ans))
print(max(ans.values()))