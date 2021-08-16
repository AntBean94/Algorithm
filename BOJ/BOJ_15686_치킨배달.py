# BOJ 15686 치킨배달

# 치킨집 정보를 좌표로 저장
# 가정집 정보도 좌표로 저장
# 조합을 통해 선별 => 최소거리 구하기

from itertools import combinations

N, M = map(int, input().split())
nom = []
chi = []
for i in range(N):
  line = list(map(int, input().split()))
  for j in range(len(line)):
    if line[j]==1:
      nom.append([j+1, i+1])
    elif line[j]==2:
      chi.append([j+1, i+1])

min_to = 100000
# M개의 치킨집 뽑아서 비교
for ch in list(combinations(chi, M)):
  total = 0
  # 각 집에서 치킨집 거리비교
  for no in nom:
    dis = 1000
    for c in ch:
      di = abs(no[0] - c[0]) + abs(no[1] - c[1])
      if di < dis:
        dis = di
    total += dis
  if total < min_to:
    min_to = total
print(min_to)

