# BOJ 21610 마법사 상어와 비바라기

''' 풀이

위의 행과 아래행, 위의 열과 아래 열은 연결되어 있다.
각 행, 열의 번호는 1부터 N까지

이동방향 (1~8)
좌, 좌상, 상, 우상, 우, 우하, 하, 좌하
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

비바라기 시전
1. 구름 생성
- 최초 구름 (N, N) 기준 (N-1, 1)(N-1, 2)(N, 1)(N, 2) 생성 
- 이후 구름 물이 2 이상인 칸, 구름이 생성된 칸은 물 2감소

2. 이동
- 모든 구름이 di 방향으로 si칸 이동

3. 이동한 칸에 비를 내려 1씩 증가시킨다.
- 이후 구름이 사라짐

4. 물이 증가한 칸에 물복사버그 시전
- 대각선방향, 경계는 넘어가면 안됨

5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름생성
- 기존에 구름이 사라진 칸에선 생성 X

================================================ 수도 코드
1. 최초 구름정보 큐에 담기

2. 이동정보 보관
- 구름정보에 이동정보(변수에 저장)를 더해서 계산
=> 위치 반환 함수, 구름정보, 이동정보

3. 구름이 사라진다.
- 구름 여부 true => false

4. 물복사버그 마법
- 대각선 [2, 4, 6, 8]
- 경계를 넘어가지 않으면 ㅇㅋ
- 주변 물당 1씩 증가

5. 구름 생성

=> 필요한 것

1. 변수) 물정보 지도 - 2차원리스트
2. 변수) 방문기록 - 2차원리스트
3. 변수) 이동전 구름정보 - 큐
4. 변수) 이동 정보 - 리스트
5. 함수) 현재 구름정보 - 함수(이동전 구름정보, 이동정보)
6. 함수) 물 복사버그 - 함수(물정보, 현재구름정보)

로직

물정보지도(초기화)
방문기록 체크(최초 구름)
구름정보(스택)

for 이동명령
    이동 후 구름정보 = [] (초기화)
    for 이동전 구름정보(뒤에서부터)
        이동정보 pop
        위치함수(구름, 이동정보)
            구름정보(스택)에 담기
        물증가
    for 이동후 구름정보
        물복사 버그함수
    새로운 구름 생성 함수(방문기록 체크)
        => 2 이상이면서 방문기록 없으면 구름정보(스택)에 담기
        => 2 이상이면서 방문기록 없으면 방문기록 삭제

'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
D = [list(map(int, input().split())) for _ in range(M)]
# 방향
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
bug_dir = [2, 4, 6, 8]
# 방문기록
V = [[0] * N for _ in range(N)]
# 이동 전 구름정보
am = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

def move_cloud(dir, dis, y, x):
    if dy[dir] < 0:
        ny = (y + dy[dir] * dis) % N
    else:
        ny = (y + dy[dir] * dis) % N
    if dx[dir] < 0:
        nx = (x + dx[dir] * dis) % N
    else:
        nx = (x + dx[dir] * dis) % N
    return ny, nx

def water_bug(y, x):
    cnt = 0
    for d in range(4):
        ny = y + dy[bug_dir[d]]
        nx = x + dx[bug_dir[d]]
        if 0 <= ny < N and 0 <= nx < N:
            if A[ny][nx]:
                cnt += 1
    return cnt

# 이동정보에 따라 함수 실행
for d, s in D:
    # 이동 후 구름정보
    pm = []
    am_l = len(am)
    for m in range(am_l-1, -1, -1):
        y, x = am.pop(m)
        # 함수
        y, x = move_cloud(d, s, y, x)
        pm.append([y, x])
        # 방문체크
        V[y][x] = 1
        # 물증가
        A[y][x] += 1
    # 물복사 버그
    for y, x in pm:
        bug = water_bug(y, x)
        A[y][x] += bug
    # 구름생성
    for i in range(N):
        for j in range(N):
            # 구름 생성
            if A[i][j] > 1 and not V[i][j]:
                A[i][j] -= 2
                am.append([i, j])
            elif V[i][j]:
                V[i][j] = 0

ans = 0
for i in range(N):
    for j in range(N):
        ans += A[i][j]
print(ans) 



         

