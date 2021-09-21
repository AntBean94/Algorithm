# BOJ 17779 게리맨더링 2

'''
구역과 인구 차이의 최솟값

1. 구역을 어떻게 나눌것인지?
- 결정해야 할 것은 r, c, d1, d2
- 20 x 20 x 20 x 20 = 1,600,000
- 둘이 합쳐서 20이 넘지않는 d1, d2를 고르기
- 이중 for문으로 구현 가능
    for i in range(20):
        for j in range(20 - i):
=> 실제 경우의 수 = 9,690개

2. 구역의 합을 어떻게 구할 것인지?
- 1) 구간합 (행) => 시간복잡도 N
- 2) 완전탐색 => 시간복잡도 N ^ 2

구간합 어떻게 구현할것인지?
조건분기
'''

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

pfs = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    tmp = 0
    for j in range(N):
        tmp += board[i][j]
        pfs[i+1][j+1] = tmp
# 기준점 고르기
ans = 1000000000
for r in range(1, N-1):
    for c in range(2, N):
        # d1은 오른쪽 범위를 결정함, d2는 왼쪽 범위를 결점함
        # d1 + d2가 높이를 결정함
        for d1 in range(1, min(N - c + 1, N - r)):
            for d2 in range(1, min(N - (r + d1) + 1, c)):
                plt = [0] * 6
                for i in range(1, N + 1):
                    # case 1. 기준점 r보다 작은경우
                    if i < r:
                        plt[1] += pfs[i][c]
                        plt[2] += pfs[i][N] - pfs[i][c]
                    # case 2. 기준점 r보다 크거나 같고 d1, d2보다 작거나 같은경우
                    elif r <= i <= min(r + d1, r + d2):
                        if r + d2 == i: plt[3] += pfs[i][c-(i-r+1)]
                        else: plt[1] += pfs[i][c-(i-r+1)]
                        plt[5] += pfs[i][c+(i-r)] - pfs[i][c-(i-r+1)]
                        plt[2] += pfs[i][N] - pfs[i][c+(i-r)]
                    # case 3. r + d1 보다 크고 r + d2보다 작거나 같을 때
                    elif r + d1 < i <= r + d2:
                        if r + d2 == i: plt[3] += pfs[i][c-(i-r+1)]
                        else: plt[1] += pfs[i][c-(i-r+1)]
                        plt[5] += pfs[i][c+d1-(i-(r+d1))] - pfs[i][c-(i-r+1)]
                        plt[4] += pfs[i][N] - pfs[i][c+d1-(i-(r+d1))]
                    # case 4. r + d2 보다 크고 r + d1보다 작거나 같을 때
                    elif r + d2 < i <= r + d1:
                        plt[3] += pfs[i][c-d2+(i-(r+d2))-1]
                        plt[5] += pfs[i][c+(i-r)] - pfs[i][c-d2+(i-(r+d2))-1]
                        plt[2] += pfs[i][N] - pfs[i][c+(i-r)]
                    # case 5. r + d1, r + d2보다 크고 가장 큰값보단 작거나 같을 때
                    elif max(r + d1, r + d2) < i <= r + d1 + d2:
                        plt[3] += pfs[i][c-d2+(i-(r+d2))-1]
                        plt[5] += pfs[i][c+d1-(i-(r+d1))] - pfs[i][c-d2+(i-(r+d2))-1]
                        plt[4] += pfs[i][N] - pfs[i][c+d1-(i-(r+d1))]
                    # case 6. 기준점 + d1 + d2 보다 클 때
                    elif i > r + d1 + d2:
                        plt[3] += pfs[i][c+(d1-d2)-1]
                        plt[4] += pfs[i][N] - pfs[i][c+(d1-d2)-1]
                # 최대, 최솟값 비교 후 정답 갱신
                result = max(plt[1:]) - min(plt[1:])
                if result < ans: 
                    ans = result

print(ans)