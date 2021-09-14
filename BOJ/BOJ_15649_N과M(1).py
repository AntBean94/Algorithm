# BOJ 15649 N과 M (1)

import sys

N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
vis = [0] * (N + 1)

def back_t(arr, cur, m):
    if m == M: sys.stdout.writelines(" ".join(map(str, cur)) + '\n')

    for a in arr:
        if not vis[a]:
            cur.append(a)
            vis[a] = 1
            back_t(arr, cur, m + 1)
            vis[a] = 0
            cur.pop()

back_t(arr, [], 0)