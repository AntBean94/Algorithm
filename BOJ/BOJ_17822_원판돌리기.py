# BOJ 17822 원판 돌리기

'''
0: 시계방향
1: 반시계방향

1. 인접수 중에서 같은 수를 모두 찾는다.
- 같은 수가 존재하면 같은 수를 모두 지운다.
- 없는 경우에는 원판에 적힌 수의 평균을 구하고, 
  평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.

원판: 50 * 50 = 2500
쿼리: 50

인접수: 4
평균 계산 및 값 수정: 50

1. 회전 절차
- x의 배수에 대해서 시행(2: 2, 4, 6, ...)
- 각 행의 기준값 인덱스를 바꾼다.
  ex) 2행 1 => 3, 4행 4 => 6 ...

2. 숫자 변경 절차
- 모든 수를 순회(순회하면서 토탈값을 구한다.)
- 인접수는 자신보다 큰 수, 오른쪽 인접수만 체크
- 인접수가 같다면 스택에 넣는다.
- 스택에서 뽑아서 0으로 바꿈
- 스택의 길이가 0이었다면 평균을 구하고 모든 값(반대 스택에 있는값)을 조정

3. 인접수 체크방법
- 기준 인덱스간의 차이 (2행, 3행) => (1, 3) = 2
- 즉, 1행 기준으로 기준인덱스가 1이고 2행이 3이면
  1행의 3번 인덱스는 2행의 5번인덱스(3 + 차이)를 확인한다.
- 같은행의 옆의값을 확인(나머지 계산으로)
- 배열 조정이 필요없기 때문에 시간복잡도 유리
'''

N, M, T = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(N)]
query = [list(map(int, input().split())) for _ in range(T)]
# 기준 인덱스
idx = [0 for _ in range(N)]

# 원판 회전
for x, d, k in query:
    n = x
    w = 1
    nd = -1 if d == 0 else 1
    # 기준 인덱스 조정(배수만큼)
    while n <= N:
        idx[n-1] += nd * k
        idx[n-1] = idx[n-1] % M
        w += 1
        n = x * w

    # 인접수 확인
    total, cnt = 0, 0
    stack, r_stack = [], []
    for i in range(N):
        for j in range(M):
            val = plate[i][j]
            # 0이면 생략
            if not val: continue
            check = 0
            up, down = -1, -1
            if i - 1 >= 0: up = (j + idx[i-1] - idx[i]) % M
            if i + 1 < N: down = (j + idx[i+1] - idx[i]) % M
            # 오른쪽 확인
            if plate[i][(j+1)%M] == val: check += 1
            # 왼쪽 확인
            elif plate[i][(j-1)%M] == val: check += 1
            # 위쪽 확인
            elif up > -1 and plate[i-1][up] == val: check += 1
            # 아래쪽 확인
            elif down > -1 and plate[i+1][down] == val: check += 1

            # 조건을 만족하면
            if check: stack.append([i, j])
            else: r_stack.append([i, j])
            total += plate[i][j]
            cnt += 1

    # 회전이 끝난뒤 숫자 조정
    if stack:
        for r, c in stack:
            plate[r][c] = 0
    else:
        if not cnt: continue
        m = total / cnt
        for r, c in r_stack:
            if plate[r][c] > m: plate[r][c] -= 1
            elif plate[r][c] < m: plate[r][c] += 1

result = 0
for p in plate:
    result += sum(p)

print(result)