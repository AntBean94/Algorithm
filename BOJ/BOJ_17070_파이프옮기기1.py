# BOJ 17070 파이프옮기기

# dfs, bfs?
# 링크로 어떻게 표현?
# 방향도 같이 넘겨줘야함
# if==lst[1][1] 이라면 연결공간이 3개 필요!
# 링크리스트, 방문기록 리스트, 방향기록
# 단방향 링크리스트

import time
start = time.time()

dir = [[0, 2], [1, 2], [0, 1, 2]]
dx = [1, 0, 1]
dy = [0, 1, 1]

# (내위치, 방향)
def find_route(M, D):
  global cnt
  # 종착점
  if M==N*N:
    cnt += 1
    return
  # 방향체크
  for di in dir[D]:
    if link[M][di]:
      find_route(link[M][di], di)

N = int(input())
link = [list() for _ in range(N * N + 1)]
box = [list(map(int, input().split())) for _ in range(N)]
# 링크리스트 만들기
for i in range(N):
  for j in range(1, N):
    chk = 0
    for d in range(3):
      if i+dy[d] < N and j+dx[d] < N and box[i+dy[d]][j+dx[d]]==0:
        if d==0: 
          if j >= N-2 and i!=N-1:
            link[i*N+j+1].append(0)
          else:
            link[i*N+j+1].append(i*N+j+2) 
        elif d==1:
          if i >= N-2 and j!=N-1:
            link[i*N+j+1].append(0)
          else:
            link[i*N+j+1].append((i+1)*N+j+1)
        elif d==2 and chk==0:
          link[i*N+j+1].append((i+1)*N+j+2)
        else:
          link[i*N+j+1].append(0)
          chk += 1
      else:
        link[i*N+j+1].append(0)
        chk += 1
cnt = 0
if box[N-1][N-1]==1:
  print(0)
else:
  find_route(2, 0)
  print(cnt)        

print("time :", time.time() - start)
