# BOJ 2473 세 용액

'''
산성, 알칼리성

산성 용액 특성값: 1 <= x <= 1,000,000,000
알칼리성 특성값: -1,000,000,000 <= y <= -1
같은 양의 세가지 용액을 혼합한 용액의 특성값은 각 특성값의 합

첫번째 방법
두 수의 완탐 + 세번째 수 이분탐색
O(N^2*LogN)
=> 시간 초과

두번째 방법
투 포인터
A를 순회
B, C를 결정한다.

'''
import sys
input = sys.stdin.readline
N = int(input())
arr = sorted(list(map(int, input().split())))

min_result = 3000000001
ans = []
for i in range(N-2):
    a = arr[i]
    l, r = i + 1, N - 1
    # 투 포인터 알고리즘
    b, c = arr[l], arr[r]
    while l != r:
        s = a + b + c
        if s == 0:
            min_result = 0
            ans = [a, b, c]
            break
        elif s > 0:
            if abs(s) < abs(min_result):
                ans = [a, b, c]
                min_result = s
            r -= 1
            c = arr[r]
        else:
            if abs(s) < abs(min_result):
                ans = [a, b, c]
                min_result = s
            l += 1
            b = arr[l]
    if min_result == 0: break
print(*sorted(ans))