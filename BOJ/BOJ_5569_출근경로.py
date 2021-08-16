# BOJ 5569 출근 경로

'''
dfs로 풀면 백트래킹을 해도 시간초과발생
2^100 = .....

DP로 풀자!

출발지점부터 거리순으로 기록?
즉, 2차원 DP

테이블을 두개로?

3차원 배열

거리 - 조합 - 이전 방향
[[[가로], [세로]], [[  ], [  ]], ...  ]

[아래에서 올라온애, 왼쪽에서 온애]
[
    [[1, 0], [1, 1], [4, 2]]  =  6
    [1, 0], [1, 1], [3, 2]
    [1, 0], [1, 1], [2, 2]
    [1, 0], [1, 1], [1, 1]
    [1, 1], [0, 1], [0, 1]
]

2차원 배열로 데이터 저장

1, 1
1, 2| 2,1
1, 3| 2, 2| 3, 1
1, 4| 2, 3| 3, 2
    | 2, 4| 3, 3
          | 3, 4

각 항목에 대해 4가지 연산 실시
[i, j] 
index[0] = i
1) 위쪽 덧셈: 현재위치 index[0] 더하기
    - arr[i + 1][j][0] += arr[i][j][0]
2) 오른쪽 덧셈: 아래의 index[0] 더하기
    - arr[i][j + 1][1] += arr[i - 1][j][0]

index[1] = j
1) 위쪽 덧셈: 왼쪽 index[1] 더하기
    - arr[i + 1][j][0] += arr[i][j - 1][1]
2) 오른쪽 덧셈: 현재위치 index[1] 더하기
    - arr[i][j + 1][1] += arr[i][j][1]

'''

import sys
input = sys.stdin.readline

# 초기값
W, H = map(int, input().split())
board = [list([0, 0] for _ in range(W)) for _ in range(H)]
board[0][0] = [1, 1]

# 좌표 정하는 함수: [위 y, 위 x, 오 y, 오 x]
def coordinate(d, y, x):
    coor = [0] * 4
    if d == 0:
        coor = [y, x, y - 1, x]
    else:
        coor = [y, x - 1, y, x]
    return coor

# 계산
for i in range(H):
    for j in range(W):
        for d in range(2):
            # 값이 0이면 지나감
            if not board[i][j][d]:
                continue
            c = coordinate(d, i, j)
            # 오른쪽 덧셈
            val = 0
            if c[2] >= 0 and c[3] >= 0:
                val = board[c[2]][c[3]][d]
            if j + 1 < W:
                board[i][j+1][1] += val
            # 위쪽 덧셈
            val = 0
            if c[0] >= 0 and c[1] >= 0:
                val = board[c[0]][c[1]][d]
            if i + 1 < H:
                board[i+1][j][0] += val

print(sum(board[H-1][W-1]) % 100000)

