# BOJ 20055 컨베이어 벨트 위의 로봇

def isEnd(ar):
  chk = 0
  for a in ar:
    if not a:
      chk += 1
  if chk >= K:
    return True
  else:
    return False
N, K = map(int, input().split())
arr = list(map(int, input().split()))
loc = []
cnt = 1
while cnt:
  T = arr.pop()
  arr = [T] + arr
  for i in range(len(loc)):
    if loc[i]+1 < N:
      loc[i] += 1
    else:
      loc.remove(loc[i])
  for i in range(len(loc)-1, -1, -1):
    if loc[i] < N:
      if arr[loc[i]]:
        if i < len(loc)-1:
          if loc[i]+1 != loc[i+1]:
            loc[i] += 1
            arr[loc[i]-1] -= 1
        else:
          loc[i] += 1
          arr[loc[i]-1] -= 1
  if len(loc) and loc[-1]==N:
    loc.pop()
  if arr[0]:
    arr[0] -= 1
    loc = [1] + loc
  if isEnd(arr):
    break
  else:
    cnt += 1
print(cnt)