# BOJ 16235 나무 재테크

''' 로직
봄, 여름, 가을, 겨울

봄
- 나무가 자신의 나이만큼 양분을 먹는다.
- 나이가 1증가한다.
- 나이가 어린 나무부터 양분을 먹는다.
- 양분을 먹을 수 없는 나무는 죽는다.

여름
- 죽은 나무가 양분으로 변한다. (죽은나무 나이 / 2 => 정수)

가을
- 나이가 5의 배수인나무는 번식한다. => 주변 8칸에 나무 1개 추가 (범위를 벗어나면 안생김)

겨울
- 양분 배열(A)에 따라 양분이 추가된다.


수도 코드
1. 데이터 입력
- 나무 데이터: 3차원리스트? => 5, 4, 3, 2, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
- 현재 양분 데이터

2. K만큼 반복
    2-1. 3중 for문을 활용 양분을 먹인다. (3번째 for문에서 뒤로탐색)
        양분을 못먹은 나무부터 -1로 바꿔가며 2로 나누고 누적양분에 더한다.
        양분을 먹은 나무는 1씩 증가 (증가값이 5의 배수이면 큐에 넣는다.)
    양분을 누적한만큼 각 위치에 더한다.

    2-2. 큐에서 하나씩 뽑아서 번식하는 함수에 투입

    2-3. 양분배열A 만큼 추가


'''
import sys
input = sys.stdin.readline
# 맵 크기, 나무 갯수, 시간
N, M, K = map(int, input().split())
# 매년 주는 양분 정보
A = [list(map(int, input().split())) for _ in range(N)]
# 현재 양분 정보(field)
F = [[5] * N for _ in range(N)]
# 나무 정보
tmp = []
for i in range(M):
    tmp.append(list(map(int, input().split())))
# 초기 셋팅
T = [list(list() for _ in range(N)) for _ in range(N)]
# tmp.sort(key=lambda x: x[2])
for y, x, z in tmp:
    T[y-1][x-1].append(z)
# 8방향
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# 번식 함수
def breed(adult, Tree):
    for y, x in adult:
        for d in range(8):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                Tree[ny][nx].append(1)
                # print('나무 앙')

# 반복문 시작
for k in range(K):
    adult = []
    # 양분 먹이기
    for i in range(N):
        for j in range(N):
            # 위치가 정해졌으므로 나무를 탐색
            num = len(T[i][j])
            neut = 0
            for t in range(num-1, -1, -1):
                y = T[i][j][t]
                # 양분이 남으면
                if y == -1:
                    break
                elif -1 < y <= F[i][j]:
                    F[i][j] -= y
                    T[i][j][t] += 1
                    if T[i][j][t] % 5 == 0:
                        adult.append([i, j])
                # 양분이 없다면
                elif y > F[i][j]:
                    neut += (y // 2)
                    T[i][j][t] = -1 
            F[i][j] += neut

    # 번식하기
    # print('adult', adult)
    breed(adult, T)

    # 양분추가
    for i in range(N):
        for j in range(N):
            F[i][j] += A[i][j]

    # 결과 출력
    # print()
    # print('F')
    # for f in F:
    #     print(f)

    # print('T')
    # for t in T:
    #     print(t)
    # print()


ans = 0
for i in range(N):
    for j in range(N):
        lth = len(T[i][j])
        for t in range(lth - 1, -1, -1):
            if T[i][j][t] > 0:
                ans += 1
            else:
                break
print(ans)

