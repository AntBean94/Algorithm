# BOJ 17471 게리맨더링

from itertools import combinations

def bfs(s, visit):
  total = 0
  total += plt[s-1]
  visit[s] = 1
  Q = []
  Q.append(s)
  while Q:
    t = Q.pop(-1)
    for v in link[t]:
      if not visit[v]:
        visit[v] = 1
        Q.append(v)
        total += plt[v-1]
  return total

N = int(input())
plt = list(map(int, input().split()))
link = [list() for _ in range(N+1)]
for n in range(1, N+1):
  arr = list(map(int, input().split()))
  for i in arr[1:]:
    link[n].append(i)
pull = sum(plt)
arr = []
ans = 1000
for i in range(N):
  arr.append(i+1)
# 모든 조합에서 각각의 경우의 수마다 visit함수를 만들고 bfs에 넣는다.
for n in range(1, N//2+1):
  for li in list(combinations(arr, n)):
    a_visit = [1] + [0 if i in li else 1 for i in range(1, N+1)] 
    b_visit = []
    for a in a_visit:
      if a:
        b_visit.append(0)
      else:
        b_visit.append(1)
    st = 0
    for u in range(1, N):
      if u not in li:
        st = u
        break
    a_total = bfs(li[0], a_visit)
    b_total = bfs(st, b_visit)
    # 이어져 있는지 확인
    if a_total+b_total==pull:
      if a_total >= b_total:
        mi = a_total - b_total
        if mi < ans:
          ans = mi
      else:
        mi = b_total - a_total
        if mi < ans:
          ans = mi
if ans==1000:
  print(-1)
else:
  print(ans)



