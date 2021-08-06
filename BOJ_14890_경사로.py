# BOJ 14890 경사로


'''
조건의 조합
내려갈 수 있는 조건
올라갈 수 있는 조건

down_condition = True 시작      V
- 내려가면 False 전환.      V
- 내려간뒤 L만큼 이동하면 True 전환     V
- 올라가면 True 유지.       V

up_condition = False 시작       V
- 내려가면 False 유지       V
- down_condition이 True로 바뀐뒤 K 적립     V
- 올라가면 False 유지       V
- 올라간뒤 K 적립(down_cnd = True이므로)       V
공통
- K가 L만큼 누적되면 True로 전환       V

경사로에서 1-up을 만나면 up condition 체크
false라면 break

경사로에서 1-down을 만나면 down condition 체크
false라면 break

'''


import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

ans = 0
# 가로 체크
for k in range(2):
    for i in range(N):
        down_cnd = True
        up_cnd = False
        if k == 0:
            back = board[i][0]
        else:
            back = board[0][i]
        K = 1
        for j in range(1, N):
            if k == 0:
                now = board[i][j]
            else:
                now = board[j][i]
            # 조건 체크
            if K >= L and not down_cnd:
                down_cnd = True
                K = 0
            elif K >= L and down_cnd:
                up_cnd = True
            # 같으면
            if now == back:
                K += 1
            # 낮으면
            elif now == back - 1:
                if not down_cnd:
                    break
                down_cnd = False
                up_cnd = False
                K = 1
            # 높으면
            elif now == back + 1:
                if not up_cnd:
                    break
                down_cnd = True
                up_cnd = False
                K = 1
            # 높이차이가 많이나면 중지
            else:
                break
            # 조건 체크
            if K >= L and not down_cnd:
                down_cnd = True
                K = 0
            elif K >= L and down_cnd:
                up_cnd = True
            # 통행 가능!
            if j == N-1 and down_cnd:
                ans += 1
            # for문 마다 back 초기화
            back = now

print(ans)