# BOJ 11066 파일 합치기

'''
접근 방법

2차원 테이블에 파일의 시작을 행으로, 끝을 열로 비용을 저장
ex) table[start][end] = Cost

2개 단위로 합쳐가며 모든 가능한 분할의 경우의수를 확인한다.
최솟값을 갱신하며 1부터 N까지의 최소비용을 산출
'''

import sys, heapq
input = sys.stdin.readline
INF = 1000000000

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    files = list(map(int, input().split()))
    table = [[0] * (N + 1) for _ in range(N + 1)]
    cum = [0] * (N + 1)
    for i in range(1, N + 1):
        cum[i] = cum[i - 1] + files[i-1]
    
    for d in range(1, N):
        for l in range(1, N - d + 1):
            r = l + d
            table[l][r] = INF
            for m in range(l, r):
                table[l][r] = min(table[l][r], table[l][m] + table[m + 1][r] + cum[r] - cum[l - 1])
    print(table[1][N])