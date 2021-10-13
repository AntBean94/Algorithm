# BOJ 7579 앱

'''
Ai mi ci

M바이트의 메모리 추가 확보를 위해 앱을 비활성화 한 경우 ci합이 최소가 되도록

5 60
30 10 20 35 40
3 0 3 5 4

냅색 알고리즘
메모리를 중심으로 계산시 10,000,000 * 100 ... => 시간초과

코스트최저중 메모리가 초과되는거?

그렇다면 코스트는 최대 10,000
=> 메모리를 기준으로 계산하면 시간초과
=> 코스트를 기준으로 계산하면 10,000 * 100 이므로 가능!

0 ~ 10,000
같은 코스트를 기준으로 메모리가 최대가 되면 갱신

Table의 아래부터 M을 넘는 최초 인덱스 출력
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mm = list(map(int, input().split()))
cost = list(map(int, input().split()))

table = [0] * 10001

for i in range(N):
    if not i:
        table[cost[i]] = mm[i]
        continue
    c = cost[i]
    tmp = []
    for n in range(10000, -1, -1):
        if not table[n] and n: continue
        k = c + n
        if table[k]: table[k] = max(table[n] + mm[i], table[k])
        else: table[k] = table[n] + mm[i]

# 메모리를 만족하는 최솟값 확인
for i in range(10001):
    if table[i] >= M:
        print(i)
        break