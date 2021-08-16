# BOJ 11052 카드 구매하기

N = int(input())
cost = [0] + list(map(int ,input().split()))
table = [0] * (N + 1)
for i in range(N):
    table[i + 1] = cost[i + 1]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i + j <= N and table[i] + cost[j] > table[i + j]:
            table[i + j] = table[i] + cost[j]
print(table[N])

