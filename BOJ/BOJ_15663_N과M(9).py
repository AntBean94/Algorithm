# BOJ 15663 N과 M (9)

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = set()

def recur(arr, ans, n, vis):
    if n == M:
        tmp = [0] * M
        for i, v in enumerate(vis):
            if v: tmp[v-1] = arr[i]
        tmp = " ".join(map(str, tmp))
        if tmp not in ans: print(tmp)
        ans.add(tmp)
        return

    for i in range(N):
        if not vis[i]:
            vis[i] = n + 1
            recur(arr, ans, n + 1, vis)
            vis[i] = 0

recur(arr, ans, 0, [0] * N)