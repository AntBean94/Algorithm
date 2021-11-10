# BOJ 1074 Z

'''
분할정복
'''

N, r, c = map(int, input().split())

def recur(h, w, y, x, total, n):
    n -= 1
    c = 2 ** n // 2
    p = 2 ** (2 * n)
    # 종료조건
    if n == -1:
        print(total)
        exit()
    # 1구역
    if y <= h and x <= w:
        recur(h - c, w - c, y, x, total, n)
    # 2구역
    elif y <= h and x > w:
        recur(h - c, w + c, y, x, total + p, n)
    # 3구역
    elif y > h and x <= w:
        recur(h + c, w - c, y, x, total + 2 * p, n)
    # 4구역
    else:
        recur(h + c, w + c, y, x, total + 3 * p, n)

center = 2 ** N // 2 - 1
recur(center, center, r, c, 0, N)