# BOJ 1806 부분합

N, S = map(int, input().split())
arr = list(map(int, input().split()))

sub = 0
for i in range(N):
    tmp = arr[i]
    arr[i] += sub
    sub += tmp

ans = 1000000
arr = [0] + arr
i, j = 0, 1
while i < j:
    sub_sum = arr[j] - arr[i]
    if sub_sum >= S:
        lth = j - i
        if lth < ans:
            ans = lth
        i += 1
    else:
        j += 1
        if j == N + 1: break

if ans == 1000000:
    print(0)
else:
    print(ans)