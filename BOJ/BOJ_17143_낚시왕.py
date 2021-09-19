# BOJ 17143 낚시왕

'''
접근방법

100 X 100 X 100 = 1,000,000

1. 상어의 이동

2. 중복상어 삭제

3. 잡을 상어 선택

어떻게 처리할까?

해시와 이차원 배열(위치)로 관리
hash = {1번상어: [y, x, 속력, 방향, 크기, 단계], 2번상어: ... }

1. 낚시왕 이동
- 기준 열 변경

2. 제일 가까운 상어 낚시
- 열 기준으로 위치배열을 탐색하며 가장 가까운 상어 번호확인
- 해당 상어 삭제, 해시 배열에서도 상어 삭제
- 정답에 크기를 누적

3. 상어 이동
- 해시값을 하나씩 뽑는다.
- 기존위치에서 번호를 삭제한다.
- 위치와 속도에 따라 이동한다.
- 바뀐위치에 있는 상어가 다른 단계라면 상어의 번호를 바꾼다.
- 같은 단계라면 크기비교후 더 큰 상어의 번호를 선정한다.
    - 이후 사라진 상어의 번호를 해시에서 삭제한다.
    - 단계를 바꿔 추가한다.

'''
import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
# 위, 아래, 오른쪽, 왼쪽
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]

sharks = {}
board = [[0] * C for _ in range(R)]
total = 0
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    # y, x, 속력, 방향, 크기, 단계
    if d == 1 or d == 2: s = s % (2 * R - 2)
    else: s = s % (2 * C - 2)
    sharks[i+1] = [r-1, c-1, s, d, z, 0]
    # 위치 기록
    board[r-1][c-1] = i + 1

# 1. 낚시왕 이동
for c in range(C):
    # 2. 제일 가까운 상어 낚시
    for r in range(R):
        shark = board[r][c]
        if shark:
            total += sharks[shark][4]
            # 2-1. 상어 삭제
            board[r][c] = 0
            del sharks[shark]
            break
    
    # 3. 상어 이동
    # value = [y, x, 속력, 방향, 사이즈, 단계 = c + 1]
    tmp = set()
    for key, value in sharks.items():
        y, x, s, d, z, t = value
        # 3-1. 기존 위치 삭제
        if board[y][x] == key: board[y][x] = 0

        # 3-2. 이동(시간초과 주범)
        while s:
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < R and 0 <= nx < C:
                y, x = ny, nx
                s -= 1
            else:
                if d == 1 or d == 3: d += 1
                else: d -= 1

        value[0] = y
        value[1] = x
        value[3] = d

        # 3-3. 바뀐 위치의 상어 확인
        if board[y][x]:
            pre_shark = board[y][x]
            # 단계 확인(다르면)
            if sharks[pre_shark][5] != c + 1:
                board[y][x] = key
                value[5] += 1
            else:
                # 같으면 크기비교
                if sharks[key][4] > sharks[pre_shark][4]:
                    board[y][x] = key
                    value[5] += 1
                    tmp.add(pre_shark)
                else:
                    tmp.add(key)
        else: 
            board[y][x] = key
            value[5] += 1
    for sh in tmp:
        del sharks[sh]

print(total)