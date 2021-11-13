# BOJ 15666 N과 M (12)

N, M = map(int, input().split())
arr = list(set(map(int, input().split())))
N = len(arr)
ans = []

def recur(arr, seq, k, l):
    if l == M:
        ans.append(sorted(seq))
        return
    for i in range(k, N):
        seq.append(arr[i])
        recur(arr, seq, i, l+1)
        seq.pop()

recur(arr, [], 0, 0)
for a in sorted(ans):
    print(*a)