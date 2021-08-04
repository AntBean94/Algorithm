# BOJ 21608 상어 초등학교

'''
인접 조건
|r1 - r2| + |c1 - c2| = 1 
=> 상, 하, 좌, 우

조건 
-조건1) 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
-조건2) 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
-조건3) 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

조건을 만족하는 자리(인접 수, 빈칸 수, y, x)를 큐에 넣는다.
(시간초과시) 인접 수, 빈칸 수 분리(인접수가 같은경우에만 빈칸 조사)
우선순위 큐에 따라 가장 앞에있는 값을 뽑아낸다.
학생번호를 기록한다.

- 모든 학생에 대해 반복

자리배치가 완료된 뒤 만족도 조사
인접학생 0 => 0
        1 => 1
        2 => 10
        3 => 100
        4 => 1000

400 * 4(주변 탐색) * log400 + 400 * 4 
N^2 * 4 * 2logN = 8 N^2 logN => N < 20이므로 괜춘
시간복잡도 문제 X
'''

import sys
input = sys.stdin.readline

N = int(input())
info = [list(map(int, input().split())) for _ in range(N**2)]


