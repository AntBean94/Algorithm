# BOJ 2304 창고다각형

T = int(input())
box = [list(map(int, input().split())) for _ in range(T)]
box = sorted(box)

# max 값, idx 찾기
idx = []
height = []
for i in box:
    idx.append(i[0])
    height.append(i[1])
maxH = max(height)
maxI = height.index(maxH) # 리스트 idx임/ idx[maxI] 로 활용
lth = len(idx)

# 직사각형 넓이(최대)
Area = (idx[-1] + 1) * maxH

# 좌측 사각형 빼기
M = 0
for i in range(maxI+1):
    if height[i] > M:
        Area -= idx[i] * (height[i] - M)
        M = height[i]

# 우측 사각형 빼기
N = height[-1]
for i in range(lth-2, maxI-1, -1):
    if height[i] > N:
        Area -= (idx[-1] - idx[i]) * (height[i] - N)
        N = height[i]

print(Area)