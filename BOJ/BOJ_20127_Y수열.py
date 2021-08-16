# BOJ 20127 Y-수열

# 문제
'''
N개의 정수로 이루어진 수열 a1, a2,..., an이 있다.
택희는 해당 수열이 증가수열 혹은 감소수열이 되게 만들고 싶다.
증가수열은 모든 i(1 <= i < N)에 대해서 ai <= ai+1 을 만족하는 수열이고, 
감소수열은 ai >= ai+1 을 만족하는 수열이다.
택희는 해당 수열의 맨 앞의 k개의 원소를 맨 뒤로 옮겨서 증가수열 또는 감소수열을 만들고 싶다. 즉, ak+1,..., aN, a1,..., ak가 증가수열, 또는 감소수열이 돼야 한다.
옮기지 않는 경우는 k=0이라고 하자. 이때, 적절한 k를 골라서 원하는 수열을 만들 수 있게 도와줘라.
'''

# 접근법
# cut & concatenation
# 1. for문 반복으로 증가, 감소여부 확인
# - 기울기가 변하는 점이 없다면 => 0 출력
# 2. 증가하다가 처음으로 감소하는 부분을 만나면 다음과 같이 자른다.
# - 기준: 미분값이 0인 숫자를 포함하는 부분의 앞뒤로 자른다.
# ex) 3 3 3 4 4 4 3 3 3
#  => 3 3 3|4 4 4|3 3 3
# 3. 1번 파트를 뒤로 보낸뒤 증가, 감소여부 체크 => 성공시 K 출력
# 4. 1+2번 파트를 뒤로 보낸뒤 체크 => 성공시 K 출력
# 5. 3, 4 번 실패시 => -1출력


# 예외처리 중요!!
'''
case 1.
10
3 3 3 3 4 3 3 3 3 3
=> 4가 정답 (5로 출력하지 않도록 주의)

case 2.
10
1 4 3 3 3 2 2 2 1 1
=> 1이 정답 (-1로 출력하지 않도록 주의)
'''

# 증가, 감소수열 판별
def check_seq(array):
  chk = 1
  fst = array[0]
  # 증가함수?
  for t in array:
    if t >= fst:
      fst = t
    else:
      chk = 0
  if chk:
    return True
  chk = 1
  # 감소함수?
  for t in array:
    if t <= fst:
      fst = t
    else:
      chk = 0
  if chk:
    return True
  else:
    return False

# 입력
N = int(input())
arr = list(map(int, input().split()))
check = 1

# 함수 투입
if check_seq(arr):
  print(0)
  check = 0

# 수정필요
if check:
  first = 0
  second = 0
  pre = arr[0]
  flow = 0
  equal = 1
  # 증가, 감소여부 확인
  for i in range(len(arr)):
    if flow:
      if flow==1:
        # 같을경우
        if arr[i]==pre:
          equal += 1
        # 증가하다 감소
        elif arr[i] < pre:
          first = i - equal
          second = i
          break
        # 증가
        else:
          equal = 1
      else:
        # 같을경우
        if arr[i]==pre:
          equal += 1
          # 감소하다 증가
        elif arr[i] > pre:
          first = i - equal
          second = i
          break
        else:
          equal = 1
    else:
      if arr[i] > pre:
        flow = 1
      elif arr[i] < pre:
        flow = -1
    pre = arr[i]

  arr1 = arr[first:] + arr[:first]
  arr2 = arr[second:] + arr[:second]

  if check_seq(arr1):
    print(first)
    check = 0
  if check:
    if check_seq(arr2):
      print(second)
      check = 0

if check:
  print('-1')


