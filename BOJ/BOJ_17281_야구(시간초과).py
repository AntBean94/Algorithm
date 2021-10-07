# BOJ 17281 야구

# 1번 선수 => 4번타자 고정
# 나머지 선수 자유롭게 조정

# 완전탐색?
# 순열(1번 제외) => 모든 경우의 수 점수 측정
# 각 타별 누적합 1, 2, 3루타 = 6 이므로 3점

from itertools import permutations
N = int(input())
seq = [list(map(int, input().split())) for _ in range(N)]

# k = 0
# for q in seq:
#   if sum(q)==32:
#     k += 1

# if k==N:
#   print(8*3*9)
# else:

per = [1, 2, 3, 4, 5, 6, 7, 8]
max_s = 0

for pm in permutations(per, 8):
  # 타순 정렬
  pm = pm[:3] + (0,) + pm[3:]
  # 이닝 시작
  score = 0
  num = 0
  for e in range(N):
    cnt = 0
    roo = [0, 0, 0]
    while cnt < 3:
      if seq[e][pm[num]]==0:
        cnt += 1
      elif seq[e][pm[num]]==1:
        score += roo.pop()
        roo = [1] + roo
      elif seq[e][pm[num]]==2:
        score += sum(roo[1:])
        roo = [0, 1] + roo[:1]
      elif seq[e][pm[num]]==3:
        score += sum(roo)
        roo = [0, 0, 1]
      else:
        score += sum(roo) + 1
        roo = [0, 0, 0]
      num += 1
      if num > 8:
        num = 0

  if score > max_s:
    max_s = score
    print(pm)
print(max_s)