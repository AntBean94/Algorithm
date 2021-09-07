# BOJ 2470 두 용액

import sys
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

i = 0
j = N - 1
X = sys.maxsize
ans = []

while i != j:
    l, r = arr[i], arr[j]
    tmp = l + r
    if tmp == 0:
        ans = [l, r]
        break
    elif tmp < 0:
        if abs(tmp) < X:
            X = abs(tmp)
            ans = [l, r]
        i += 1
    else:
        if abs(tmp) < X:
            X = abs(tmp)
            ans = [l, r]
        j -= 1
print(*ans)