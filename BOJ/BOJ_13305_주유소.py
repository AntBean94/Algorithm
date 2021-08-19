# BOJ 13305 주유소

N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

ans = 0
oil = 1000000000
for i in range(N-1):
    if price[i] < oil:
        oil = price[i]
    ans += (oil * road[i])
print(ans)