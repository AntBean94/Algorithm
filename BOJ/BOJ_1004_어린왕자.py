# BOJ 1004 어린 왕자

'''
1. 장미와 어린왕자가 서로 다른 원에 있으면 카운트
2. 장미와 어린왕자가 같은 원에 있거나 없으면 패스
'''

import sys
input = sys.stdin.readline

# 거리계산 함수
def cal(x1, y1, cx, cy, r):
    dist = ((x1 - cx) ** 2 + (y1 - cy) ** 2) ** (1/2)
    if dist < r: return True
    else: return False

T = int(input())
for tc in range(T):
    ans = 0
    # 출발점(x1, y1), 도착점(x2, y2)
    x1, y1, x2, y2 = map(int, input().split())
    # 행성계의 개수
    N = int(input())
    # 행성계의 중점과 반지름(cx, cy, r)
    planets = [list(map(int, input().split())) for _ in range(N)]
    
    # 각 행성계의 중점과 출발점, 도착점 거리비교
    for cx, cy, r in planets:
        # 출발점 비교
        case1 = cal(x1, y1, cx, cy, r)
        # 도착점 비교
        case2 = cal(x2, y2, cx, cy, r)
        # 서로 다른 행성계인경우 +=1
        if case1 != case2: ans += 1

    # 정답 출력
    print(ans)