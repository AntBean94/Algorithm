# BOJ 17404 RGB거리 2

'''
규칙
1. 1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
2. N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
3. i(2 <= i <= N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.



'''
import sys
input = sys.stdin.readline

N = int(input())
C = [list() for _ in range(N)]

'''
6
10 20 30
10 20 30
10 20 30
10 20 30
10 20 30
10 20 30

3
10 50 50
15 15 15
10 50 50

3
13 89 99
49 60 57
26 40 83

2
1000 1000 1
1000 1000 1

'''