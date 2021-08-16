# BOJ 1080 행렬

def reverse(row, col):
  for s in range(3):
    for t in range(3):
      if RC[row+s][col+t]=='1':
        RC[row+s] = RC[row+s][:col+t] + '0' + RC[row+s][col+t+1:]
      else:
        RC[row+s] = RC[row+s][:col+t] + '1' + RC[row+s][col+t+1:]

N, M = map(int, input().split())
RC = []
cnt = 0
for _ in range(N*2):
  RC.append(input())
for r in range(N):
  for c in range(M):
    if RC[r][c] != RC[r+N][c]:
      # 실패여부
      if r > N-3 or c > M-3:
        cnt = -1
        break
      # 함수투입
      else:
        reverse(r, c)
        cnt += 1
  if cnt==-1:
    break
print(cnt)

