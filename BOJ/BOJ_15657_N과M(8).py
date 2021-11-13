# BOJ 15657 N과 M (8)

N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = []

def recur(arr, seq, t, k):
    if k == M:
        ans.append(sorted(seq))
        return
    for i in range(t, N):
        seq.append(arr[i])
        recur(arr, seq, i, k+1)
        seq.pop()

recur(arr, [], 0, 0)
for a in sorted(ans):
    print(*a)