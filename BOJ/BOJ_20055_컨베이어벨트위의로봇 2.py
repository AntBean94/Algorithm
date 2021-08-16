# BOJ 20055 컨베이어 벨트 위의 로봇

# 조건
# 로봇이 올라가면 내구도 1감소, 로봇이 이동하면 내구도 1감소
''' 절차
# 1. 벨트 회전
# 2. 로봇이동
# 3. 로봇 올리기
# 4. 내구도 체크 및 과정 종료
# 각 과정별로 내구도가 0인 캇의 갯수를 체크 => K개 이상이라면 종료, 과정체크
'''

# 풀이
# 단계별로 함수를 만들어서 투입(각 함수진행시 cnt 1증가, 종료조건 체크)
# 1. 벨트 회전 함수
# - 맨뒤를 빼서 앞으로 보낸다.
# 2. 위에 로봇이 있다면 한칸 이동(내구도 감소)/ => 조건) 내구도 1이상
# - 이동여부 체크 구간 range(1, len(N))
# 3. 올라가는 위치에 로봇을 올린다(내구도 감소)/ => 조건) 내구도 1이상
# 4. 내구도 체크 및 종료/ 1번 함수로 이동


# 종료조건 함수
def isEnd(ar):
  chk = 0
  for a in ar:
    if not a:
      chk += 1
  if chk >= K:
    return True
  else:
    return False


# 벨트 길이, 0칸 갯수 기준 
N, K = map(int, input().split())
# 칸별 내구도
arr = list(map(int, input().split()))
loc = []
cnt = 1
while cnt:
  # 1단계
  T = arr.pop()
  arr = [T] + arr
  # 컨베이어 이동으로 로봇위치변동
  for i in range(len(loc)):
    if loc[i]+1 < N:
      loc[i] += 1
    else:
      loc.remove(loc[i])
  
  # 2단계
  # 한칸 앞으로 이동(내구도체크, 앞에 로봇체크) => 뒤에서 for문
  for i in range(len(loc)-1, -1, -1):
    # 마지막위치로봇 여부 체크
    if loc[i] < N:
      # 앞칸 내구도 and 앞의로봇 체크
      if arr[loc[i]]:
        # 맨 앞 로봇이 아닌경우
        if i < len(loc)-1:
          if loc[i]+1 != loc[i+1]:
            loc[i] += 1
            arr[loc[i]-1] -= 1
        # 맨 앞 로봇인경우
        else:
          loc[i] += 1
          arr[loc[i]-1] -= 1
  if len(loc) and loc[-1]==N:
    loc.pop()

  # 3단계
  # 내구도 확인 후 로봇올리기
  if arr[0]:
    arr[0] -= 1
    loc = [1] + loc
  # 검증
  if isEnd(arr):
    break
  else:
    cnt += 1

print(cnt)

