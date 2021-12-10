# BOJ 10815 숫자 카드

N = int(input())
nums = set(map(int, input().split()))
M = int(input())
ans = ""
for i in map(int, input().split()):
    if i in nums: ans += "1 "
    else: ans += "0 "
print(ans)