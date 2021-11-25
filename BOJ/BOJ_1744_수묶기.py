# BOJ 1744 수 묶기

'''
단순하게 생각하면

음수끼리 곱 (작은 수로 정렬한다음)
양수끼리 곱 (큰 수로 정렬한다음)

0은 음수랑 곱하면 좋음

1이 하나라도 포함된 경우 덧셈
'''

N = int(input())
arr_p = []
arr_m = []
zero_cnt = 0

for i in range(N):
    n = int(input())
    if n > 0: arr_p.append(n)
    elif n < 0: arr_m.append(n)
    else: zero_cnt += 1

arr_p.sort(reverse=True)
arr_m.sort()
ans = 0
# 양수
for i in range(0, len(arr_p), 2):
    if i == len(arr_p) - 1:
        ans += arr_p[i]
        break
    if arr_p[i] == 1 or arr_p[i + 1] == 1:
        ans += arr_p[i] + arr_p[i + 1]
    else:
        ans += arr_p[i] * arr_p[i + 1]

# 음수
for i in range(0, len(arr_m), 2):
    if i == len(arr_m) - 1:
        if zero_cnt: zero_cnt -= 1
        else: ans += arr_m[i]
        break
    ans += arr_m[i] * arr_m[i + 1]
print(ans)