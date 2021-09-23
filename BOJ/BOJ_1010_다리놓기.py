# BOJ 1010 다리 놓기

'''
DP로 풀어보기(연습)
조합 공식을 쓰면 훨씬 빠르게 풀 수 있음
'''


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    table = [[0] * (M + 1) for _ in range(N + 1)]
    # 테이블 초기화
    for i in range(M):
        table[1][i + 1] = 1
    # DP
    for i in range(1, N):
        for j in range(1, M):
            for k in range(j + 1, M+1):
                table[i+1][k] += table[i][j]
            
    print(sum(table[N]))