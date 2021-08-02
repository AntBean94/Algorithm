# BOJ 14501 퇴사 

# Dynamic Programming

''' 아이디어
1. 배열의 뒤에서부터 체크
2. 날짜를 체크한다.
3. 3일이면 3일 전의 값에 더한 값과 어제까지의 값과 비교
4. 더 큰 값을 적용한다.
5. 맨 앞의 수 까지 반복
'''

import sys
input = sys.stdin.readline

N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]

# 누적 수익
revenue = [0] * (N+1)

for i in range(N-1, -1, -1):
    t = schedule[i][0]
    p = schedule[i][1]
    # 일정을 초과하면 스킵
    if i + t > N:
        revenue[i] = revenue[i+1]
        continue
    # 비교(오늘 + t만큼 뺀날 vs 어제/없으면 더하기)
    if p + revenue[i+t] > revenue[i+1]:
        revenue[i] = p + revenue[i+t]
    else:
        revenue[i] = revenue[i+1]
print(revenue[0])
