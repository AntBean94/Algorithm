# BOJ 2231 분해합

n = int(input())
ans = 0
for i in range(max(1, n-54), n):
    if sum(map(int, str(i))) + i ==n:
        ans = i
        break
print(ans)

        