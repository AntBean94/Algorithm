# BOJ 2170 선 긋기

'''
1. 시작점을 기준으로 정렬한다.

2. 점을 하나씩 탐색한다. O(N)

3. 조건 
1) 점의 시작점이 이전 점의 끝점보다 큰 경우
    - ans에 이전점의 시작점과 끝점의 차이만큼 기록
    - 시작점과 끝점 수정
2) 점의 시작점이 이전 점의 끝점보다 작은 경우 & 끝점이 이전점의 끝점보다 큰 경우
    - 시작점은 유지
    - 끝점은 변경된 점에 맞게 수정

4. 누적값 출력
'''

import sys
import heapq
input = sys.stdin.readline

N = int(input())
line = []
for i in range(N):
    a, b = map(int, input().split())
    heapq.heappush(line, [a, b])

ans = 0
pre_st, pre_end = line[0][0], line[0][1]

for i in range(1, N):
    start, end = line[i]
    # 시작점이 이전 끝점보다 큰경우 추가 후 초기화
    if start > pre_end:
        ans += pre_end - pre_st
        pre_st, pre_end = start, end
    # 이전 점의 끝점보다 작은 경우 & 끝점이 이전 점의 끝점보다 큰경우
    elif end > pre_end:
        pre_end = end

ans += pre_end - pre_st
print(ans)