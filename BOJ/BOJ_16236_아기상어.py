# BOJ 16236 아기상어

# - 상어위치 저장(1차원 숫자위치로)
# - 상어 사이즈 저장
# - 상어 경험치 저장
# - 이동시간 저장

# 1. 링크리스트 만들기
# - 물고기사이즈보다 작으면 서로 연결
# - 링크는 상, 좌, 우, 하 순서로 만든다.
# - 링크는 2차원배열, 1차 깊이가 각 배열의 고유번호
# 2. visit리스트 만들기
# 3. bfs통과
# - visit리스트에 거리기록
# - 자신보다 작은크기의 물고기만나면 visit거리 저장
# - 먹은 물고기자리를 0으로 바꿈
# - 먹은 물고기자리를 상어위치에 저장
# - 상어 경험치 += 1
# - 상어 사이즈 증가여부 확인(경험치==사이즈 => 사이즈+1, 경험치초기화)
# - visit리스트 초기화
# 4. 반복
# 5. 상어가 먹이를 못찾고 나오면 이동시간 출력

def coor(M):
  a = (M-1) // N
  b = 0
  if M % N:
    b = M % N - 1
  else:
    b = N - 1
  return [a, b]

def bfs(L):
  global size
  global exp
  global time
  global lctn
  visit[L] = 1
  Q = []
  Q.append([visit[L], L])
  cnt = 0
  depth = 10000
  X = []
  while Q:
    Q.sort()
    T = Q.pop(0)
    print(T)
    if T[0] <= depth:
      for t in link[T[1]]:
        if not visit[t]:
          # 길을 지나는 경우
          loc = coor(t)
          if box[loc[0]][loc[1]]==0 or box[loc[0]][loc[1]]==size:
            visit[t] = T[0] + 1
            Q.append([visit[t], t])
          # 자기보다 작은 물고기를 만난경우
          elif box[loc[0]][loc[1]] < size:
            visit[t] = T[0]
            depth = T[0]
            X.append([visit[t], t])
            cnt+=1
    else:
      break
  if X:
    X.sort()
    S = X.pop(0)    
    time += S[0]
    loc = coor(S[1])
    box[loc[0]][loc[1]] = 0
    me = coor(lctn)
    box[me[0]][me[1]] = 0
    lctn = S[1]
    exp += 1 
    if exp==size:
      size += 1
      exp = 0

  if cnt:
    return True
  else:
    return False

N = int(input())
box = [list(map(int, input().split())) for _ in range(N)]
# 0. 위치, 좌표, 사이즈, 경험치, 시간
lctn = 0
size = 2
exp = 0
time = 0

# 상, 좌, 우, 하
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

check = True
# 여기에 상어가 물고기 찾았는지 여부 변수두고 그 변수로 while반복문 ㄱ
while check:
  link = [list() for _ in range(N*N+1)]
  # 1. 링크리스트 만들기
  for i in range(N):
    for j in range(N):
      # 통과 가능위치
      if box[i][j] <= size or box[i][j]==9:
        if box[i][j]==9:
          lctn = i*N+j+1
        for d in range(4):
          if 0 <= i+dy[d] < N and 0 <= j+dx[d] < N and (box[i+dy[d]][j+dx[d]] <= size or box[i+dy[d]][j+dx[d]]==9):
            if d==0:
              link[i*N+j+1].append((i-1)*N+j+1)
            elif d==1:
              link[i*N+j+1].append(i*N+j)
            elif d==2:
              link[i*N+j+1].append(i*N+j+2)
            else:
              link[i*N+j+1].append((i+1)*N+j+1)
  # 2. visit 리스트 만들기
  visit = [0] * (N*N+1)
  # 3. bfs 통과
  check = bfs(lctn)

print(time)