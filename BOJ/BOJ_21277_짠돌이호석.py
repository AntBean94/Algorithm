# BOJ 21277 짠돌이 호석

'''
50 * 50
2500

1. 하나의 넓은판에 퍼즐1을 배치
2. 퍼즐2를 돌려가며 퍼즐1과 비교한다.
3. 겹치는 범위만 확인하면 됨.

4. 정사각형이라고 하더라도 모서리대 모서리는 비교할 필요가 없음

기준 최솟값을 정해둔다.

수평
max(N1, N2) * (M1 + M2)
max(N1, M2) * (M1 + N2)

수직
(N1 + N2) * max(M1 + M2)
(N1 + M2) * max(M1 + N2)

이후 수정 필요
'''

import sys
input = sys.stdin.readline

# 입력값 저장
N1, M1 = map(int, input().split())
B1 = [input().rstrip() for _ in range(N1)]
N2, M2 = map(int, input().split())
B2 = [input().rstrip() for _ in range(N2)]

# 겹치지 않은 상태의 최소비용
cost = min(
    max(N1, N2) * (M1 + M2),
    max(N1, M2) * (M1 + N2),
    (N1 + N2) * max(M1, M2),
    (N1 + M2) * max(M1, N2)
)

# 퍼즐 회전 함수
def trans(arr, y, x):
    result = []
    for i in range(x-1, -1, -1):
        tmp = ""
        for j in range(y):
            tmp += arr[j][i]
        result.append(tmp)
    return result, x, y

# 퍼즐 매칭 함수
def matching(B1, B2, r, c, ovr, ovc):
    if N1 > N2:
        b1y = max(0, r - min(N1, N2))
        b2y = max(0, min(N1, N2) - r)
    else:
        b1y = max(0, r - max(N1, N2))
        b2y = max(0, min(N1, N2) - r)
    if M1 > M2:
        b1x = max(0, c - min(M1, M2))
        b2x = max(0, c - max(M1, M2))
    else:
        b1x = max(0, c - max(M1, M2))
        b2x = max(0, c - max(M1, M2))
    for i in range(ovr):
        for j in range(ovc):
            if B1[i+b1y][j+b1x] == "1" and B2[i+b2y][j+b2x] == "1":
                return False
    return True

# 최소넓이보다 작은 범위 안에서 두 퍼즐을 겹친 뒤 비교
# 4가지 방향으로 비교
for d in range(4):
    if d: B2, N2, M2 = trans(B2, N2, M2)
    # 퍼즐 이동을 위한 for문
    for i in range(1, N1 + N2):   # 높이 겹치는 부분
        ovr = min(i, N1 + N2 - i, N1, N2)
        for j in range(1, M1 + M2):   # 가로 겹치는 부분
            ovc = min(j, M1 + M2 - j, M1, M2)
            # 최소 비용 갱신가능 여부
            new_cost = (N1 + N2 - ovr) * (M1 + M2 - ovc)
            if new_cost >= cost: continue
            # 매칭을 위한 for문
            if matching(B1, B2, i, j, ovr, ovc):
                cost = new_cost
print(cost)