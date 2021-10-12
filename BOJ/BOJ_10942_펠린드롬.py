# BOJ 10942 펠린드롬?

'''
사전에 계산이 되어있어야 한다.
2차원 배열

1 2 1 3 1 2 1

각 포인트를 중심으로 좌우로 뻗어나가면서 체크
'''
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
table = [[0] * N for _ in range(N)]

def palindrome_odd(table, arr, p):
    # point index를 기준으로 양옆으로 이동
    l, r = p, p
    while l >= 0 and r < N:
        if arr[l] == arr[r]:
            table[l][r] = 1
        else: break
        l, r = l - 1, r + 1

def palindrome_even(table, arr, p):
    l, r = p, p + 1
    while l >= 0 and r < N:
        if arr[l] == arr[r]:
            table[l][r] = 1
        else: break
        l, r = l - 1, r + 1

for i in range(N):
    palindrome_odd(table, arr, i)
    if i == N-1: continue
    palindrome_even(table, arr, i)

# lets go!
ans = ''
for i in range(int(input())):
    a, b = map(int, input().split())
    # 펠린드롬 체크
    ans += f'{table[a-1][b-1]}\n'
sys.stdout.write(ans)