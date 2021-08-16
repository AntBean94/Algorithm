# BOJ 20056 마법사 상어와 파이어볼

# 연결 큐 함수
def check(Q):
  if Q > N:
    return Q % N
  elif Q < 1 :
    while Q < 1:
      Q += N
    return Q
  else:
    return Q

def movemove(arr, k):
  if k==0 or len(arr) <= 1:
    return arr

  Nrr = []
  print(4-k, '단계')
  print('시작', arr)
  print()

#################################################
  # 1. 이동
  for ball in arr:
    # 볼의 y좌표 = y좌표 + 속력 * 방향
    ball[0] = check(ball[0] + ball[3] * dy[ball[4]])
    ball[1] = check(ball[1] + ball[3] * dx[ball[4]])

  print('이동', arr)
  print()
  ################################################
  # 2-1. 중복 확인
  lth = len(arr)
  mslist = []
  for i in range(lth):
    cnt = 1
    mass = arr[i][2]
    speed = arr[i][3]
    dirlist = [arr[i][4]]

    for j in range(i+1, lth):
      # 위치가 같다면
      if arr[i][0]==arr[j][0] and arr[i][1]==arr[j][1] and j not in mslist:
        cnt += 1
        mass += arr[j][2]
        speed += arr[j][3]
        dirlist.append(arr[j][4])
        mslist.append(j)

    if cnt > 1:
      mslist.append(i)
    elif cnt==1 and i not in mslist:
      Nrr.append(arr[i])

    if cnt > 1 and mass//5:
      # 추가 코드
      chk = 0
      for d in dirlist:
        if d % 2:
          chk += 1
      dir = []
      if chk==0 or chk==cnt:
        dir = al
      else:
        dir = la
      
      mass = mass // 5
      speed = speed // cnt

      for l in range(4):
        Nrr.append([arr[i][0], arr[i][1], mass, speed, dir[l]])

  print('합체 후 나눠서 리스트에 추가', Nrr)
  print()

  return movemove(Nrr, k-1)

# 데이터 입력
N, M, K = map(int, input().split())
Fball = [list(map(int, input().split())) for _ in range(M)]

# ball = [행(y), 열(x), 질량(m), 속력(s), 방향(d)]
# 방향자(12시부터 시계방향으로)
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
al = [0, 2, 4, 6]
la = [1, 3, 5, 7]

ans = movemove(Fball, K)
print(ans)
#############################################
# 합친 뒤 출력하기
total = 0
for ball in ans:
  total += ball[2]
print(total)