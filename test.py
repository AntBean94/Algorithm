from itertools import combinations as comb
import sys
input = sys.stdin.readline
N, M, H = map(int, input().split())
ledder = [[0] * (H+1) for _ in range(N+1)]
for m in range(M):
    a, b = map(int, input().split())
    ledder[b][a] = b + 1
    ledder[b + 1][a] = b
ans = 100000000

def check(ledder, row):
    isP = []
    for i in ledder[row]:
        if i:
            if isP:
                if isP[-1] == i:
                    isP.pop(-1)
                else:
                    isP.append(i)
            else:
                isP.append(i)
    if isP:
        return False
    else:
        return True

def cal_case(ledder, row, stack):
    cnt = 0
    for i in range(1, H+1):
        if ledder[row][i]:
            cnt += 1
        else:
            if row + 1 <= N and not ledder[row+1][i]:
                stack.append(i)
    if cnt % 2:
        return 1
    else:
        return 0

def backT(ledder, r, line, k):
    global ans
    if line > k:
        return
    if r == N+1:
        if line < ans:
            ans = line
            if ans == 0:
                print(ans)
                exit()
        return
    stack = []
    s = cal_case(ledder, r, stack)

    for i in range(s, 3, 2):
        for case in comb(stack, i):
            for c in list(case):
                ledder[r][c] = r + 1
                ledder[r+1][c] = r
                line += 1
            if check(ledder, r):
                backT(ledder, r + 1, line, k)
            for c in case:
                ledder[r][c] = 0
                ledder[r+1][c] = 0
                line -= 1
    return 
    
for k in range(4):
    backT(ledder, 1, 0, k)
    if ans < 4:
        print(ans)
        break
if ans > 3:
    print(-1)
