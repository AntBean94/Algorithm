# BOJ 17386 선분 교차 1

INF = 100000000

def check(target, a, b):
    # 정렬
    if a > b: a, b = b, a
    if a <= target <= b: return True
    else: return False

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# 직선의 기울기
dx1, dy1 = x1 - x2, y1 - y2
dx2, dy2 = x3 - x4, y3 - y4
grad1 = INF if not dx1 else dy1 / dx1
grad2 = INF if not dx2 else dy2 / dx2

# 직선의 절편(INF인 경우 처리)
if grad1 == INF: pass
else: c1 = y1 - grad1 * x1
if grad2 == INF: pass
else: c2 = y3 - grad2 * x3

# 판별
# 1. 기울기가 다른 경우
if grad1 != grad2:
    # 교차점 구하기
    if grad1 == INF and grad2 != INF:
        # x고정
        cx = x1
        cy = cx * grad2 + c2
    elif grad2 == INF and grad1 != INF:
        cx = x3
        cy = cx * grad1 + c1
    else:
        cx = round((c2 - c1) / (grad1 - grad2), 10)
        cy = cx * grad1 + c1
    # 두 직선의 교차점이 두 직선의 구간안에 모두 포함되는 경우
    if check(cx, x1, x2) and check(cx, x3, x4) and check(cy, y1, y2) and check(cy, y3, y4):
        print(1)
    else:
        print(0)
# 2. 기울기가 같은 경우
else:
    # 절편이 같고 구간이 겹치는 경우
    if grad1 == INF or c1 == c2:
        if check(x1, x3, x4) and check(y1, y3, y4) or check(x2, x3, x4) and check(y2, y3, y4) or check(x3, x1, x2) and check(y3, y1, y2) or check(x4, x1, x2) and check(y4, y1, y2):
            print(1)
        else:
            print(0)
    else:
        print(0)