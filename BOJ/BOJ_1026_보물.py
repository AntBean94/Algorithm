# BOJ 1026 보물

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
ans = 0
for i in range(N):
    ans += A[i] * B[-i-1]
print(ans)