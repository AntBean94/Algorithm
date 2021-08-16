# BOJ 1002 터렛

# 둘사이의 거리 > r1 + r2 | 만나지 않는 경우 : 0
# 둘사이의 거리 = r1 + r2 | 1번 만나는 경우 : 1
# 둘사이의 거리 < r1 + r2 | 2번 만나는 경우 : 2
# 둘의 위치가 같은데 거리가 다른경우 : 0
# 둘의 위치가 같은데 거리가 같은경우 : -1

T = int(input())
for _ in range(T):
    x, y, r, X, Y, R = map(int, input().split())
    dis = (x-X)**2 + (y-Y) ** 2
    mdis = (r + R)**2
    Br, br = 0, 0
    if r > R:
        Br = r
        br = R
    else:
        Br = R
        br = r
    ans = 0
    if dis:
        if dis > mdis:
            ans = 0
        elif dis==mdis:
            ans = 1
        else:
            if (Br-br)**2==dis:
                ans = 1
            elif (Br-br)**2 > dis:
                ans = 0
            else:
                ans = 2
    else:
        if r==R:
            ans = -1
        else:
            ans = 0
    print(ans)

