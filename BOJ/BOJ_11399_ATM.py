# BOJ 11399 ATM

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
pre = 0
for i in range(N):
    pre += arr[i]
    ans += pre
print(ans)