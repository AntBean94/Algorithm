# BOJ 1107 리모컨

'''
완전탐색: 실행속도 느림
많은 조건 분기: 실행속도 빠름(예외처리 복잡)
'''

N = int(input())
M = int(input())
broken = [1] * 10
if M:
    for i in list(map(int, input().split())):
        broken[i] = 0

def check(x):
    for i in str(x):
        if not broken[int(i)]: return False
    return True

ans = 1000000
if check(N): ans = len(str(N))
# 큰 수
small = N - 1
while small >= 0:
    if check(small):
        ans = min(N - small + len(str(small)), ans)
        break
    small -= 1
big = N + 1
big_cnt = 0
while big <= 1000000 and big_cnt < ans:
    if check(big):
        big_cnt = big - N + len(str(big))
        ans = min(big_cnt, ans)
        break
    big += 1
print(min(ans, abs(100 - N)))