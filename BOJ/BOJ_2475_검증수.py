# BOJ 2475 검증수

arr = list(map(int, input().split()))
total = 0
for i in arr:
    total += i**2
ans = total % 10
print(ans)