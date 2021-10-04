# BOJ 19237 어른 상어

'''
상어
1 이상 M이하의 번호
1번 상어가 가장 강력

N: 격자 크기
M: 상어 마릿 수

냄새는 k번 이동후 사라짐

상어는 인접한 칸 중 아무 냄새가 없는 칸을 선호함
그런 칸이 없다면 자신의 냄새가 있는 칸의 방향
가능한 칸이 여려개일 경우 특정한 우선순위를 따름

상어의 초기 방향은 입력으로 주어짐

모든 상어가 이동한 후 한 칸에 여러마리의 상어가 남아있으면,
가장 강력한 상어(번호가 작은)를 제외하고 모두 아웃

1, 2, 3, 4: 위, 아래, 왼쪽, 오른쪽

결과 출력
1번 상어만 격자에 남게 되기까지 걸리는 시간을 출력
1,000초가 넘어도 1만 남아있지 않다면 -1 출력

접근 방법
1. 우선순위 정보담는 배열(3차원 배열)
[
    [[1, 2, 3, 4], [], [], []],
    [],
    [],
    .
    .
]

프로세스
- 2중 for문으로 순회 배열 순회
- 체취인 경우 k를 1줄이고 0인경우 없앤다. (3, 0) => (0, 0)
- 상어인 경우
    - 상어 위치에 k를 줄인다.
    - 우선순위와 빈칸, 자신의 체취정보를 참고해 적합한 위치를 큐에 담는다.
- 큐에 담긴 정보를 활용해 상어의 위치를 이동시킨다.
    - 같은 위치에 상어가 있고 번호가 크면 상어 정보를 갱신
    - 번호가 작다면 생략
    - 상어가 사라질때마다 cnt 하나씩 감소
- 1번상어만 남았는지 확인
    - cnt 변수를 확인해서 1이면 시간 출력
    - break

시간복잡도 = 1000 x 400 x 4 = 160만 통과 가능

문제
체취와 상어를 어떻게 구별할 것인지?
이동가능한 위치에 상어를 바로 그리는것이 아니라
상어를 큐에 담았다가 한번에 뽑아서 그린다?
=> 체취가 남아있던 자리에 이동한 상어와 빈칸으로 이동한 상어를 구별 가능

'''

import sys
input = sys.stdin.readline

N, M, k = map(int, input().split())
# 체취 1남았을 때 체크를 위해 1추가
k += 1
board = [list([0, 0, 0] for _ in range(N)) for _ in range(N)]
info = {i: [0, 0, 0] for i in range(1, M + 1)}
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        shark = line[j]
        if shark: info[shark] = [i, j, 0]; board[i][j] = [shark, k, 0]
dir_info = list(map(int, input().split()))
for i in range(M): info[i+1][2] = dir_info[i] - 1
prf = {}
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for i in range(M):
    prf[i+1] = []
    for j in range(4):
        line = list(map(int, input().split()))
        for l in range(4): line[l] -= 1
        prf[i+1].append(line)

# 방향 찾는 함수
def find_dir(board, info, id, turn):
    y, x, d = info[id]
    tmp = []
    # 선호하는 방향(현재 방향 기준)
    for nd in prf[id][d]:
        ny, nx = y + dy[nd], x + dx[nd]
        # 외부로 나가는지 확인
        if 0 <= ny < N and 0 <= nx < N:
            # 체취 없는지 확인
            if not board[ny][nx][0]:
                info[id] = [ny, nx, nd]
                return [ny, nx, id]
            # 체취가 1이면서 자신의 턴보다 1이하인경우(k + 1했기때문에 확인 가능)
            elif board[ny][nx][1] == 1 and board[ny][nx][2] < turn:
                info[id] = [ny, nx, nd]
                return [ny, nx, id]
            # 체취가 존재하지만 자신의 체취인 경우
            elif board[ny][nx][0] == id:
                if not tmp: tmp = [ny, nx, nd]
    # 다음 위치와 상어번호 리턴
    if tmp: 
        info[id] = tmp
        return [tmp[0], tmp[1], id]
    else: 
        return [y, x, id]

cnt = M
ans = 0
# 1000번째 턴까지 실행
for t in range(1, 1001):
    # 배열 순회
    sharks = []
    for i in range(N):
        for j in range(N):
            # 지정위치 턴 증가
            board[i][j][2] += 1
            # 상어또는 체취인 경우
            shark = board[i][j]
            if shark[0]:
                # 상어인 경우
                if shark[1] == k:
                    # 상어 이동 가능한 위치 반환(위치, 상어 번호)
                    loc = find_dir(board, info, shark[0], t)
                    # 스택에 추가
                    sharks.append(loc)
                # 체취 1감소
                board[i][j][1] -= 1
                # 체취가 0이 된 경우 정보 갱신
                if board[i][j][1] == 0:
                    board[i][j][0] = 0
    # 상어 배치
    for y, x, s in sharks:
        if board[y][x][0] and board[y][x][0] != s:
            if s < board[y][x][0]:
                board[y][x] = [s, k, t]
            cnt -= 1
        else:
            board[y][x] = [s, k, t]
    # 상어 마릿수 체크
    if cnt == 1:
        ans = t
        break

if ans: print(ans)
else: print(-1)    