# BOJ 2473 세 용액

'''
산성, 알칼리성

산성 용액 특성값: 1 <= x <= 1,000,000,000
알칼리성 특성값: -1,000,000,000 <= y <= -1

같은 양의 세가지 용액을 혼합한 용액의 특성값은 각 특성값의 합

같은 값을 중복사용하는것도 가능

두 수의 완탐 + 세번째 수 이분탐색
O(N^2 LogN)

=> 시간 초과

'''
import bisect
import sys
input = sys.stdin.readline
N = int(input())
arr = sorted(list(map(int, input().split())))

min_result = 3000000001
ans = []
for i in range(N):
    a = arr[i]
    for j in range(i+1, N):
        b = arr[j]
        p = a + b
        # 이분탐색으로 최적값 찾기
        idx = bisect.bisect_left(arr[j+1:], -p)
        if idx == N - j - 1:
            total = p + arr[j+idx]
        elif idx == 0:
            total = p + arr[j+1]
        else:
            if abs(p + arr[j + idx]) < abs(p + arr[j + idx + 1]):
                total = p + arr[j + idx]
            else:
                total = p + arr[j + idx + 1]
        if abs(total) < abs(min_result):
            min_result = total
            ans = [a, b, total - p]
            if total == 0: break
print(*sorted(ans))