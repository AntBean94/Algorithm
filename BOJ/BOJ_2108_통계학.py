# BOJ 2108 통계학

'''
1. 산술평균: N개의 수들의 합을 N으로 나눈 값
2. 중앙값: N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
3. 최빈값: N개의 수들 중 가장 많이 나타나는 값
4. 범위: N개의 수들 중 최댓값과 최솟값의 차이

'''
import sys
input = sys.stdin.readline

total = 0
mid = []
many = {}

N = int(input())
for i in range(N):
    n = int(input())
    total += n
    mid.append(n)
    if n in many: many[n] += 1    
    else: many[n] = 1

mid.sort()
# 1. 산술 평균
print(int(round(total / N, 0)))
# 2. 중앙값
print(mid[N//2])
# 3. 최빈값
ans = -100000
check = []
for key, value in many.items():
    if value > ans: 
        check = [key]
        ans = value
    elif value == ans: check.append(key)
if len(check) > 1: print(sorted(check)[1])
else: print(check[0])
# 4. 범위
print(mid[-1] - mid[0])