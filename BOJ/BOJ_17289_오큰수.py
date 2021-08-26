# BOJ 17289 오큰수

'''
오큰수

오큰수 체크 
1. 수열의 숫자를 하나씩 체크한다.(num)
(1). 스택이 채워져있으면서 top이 num보다 작은경우 다음을 반복
    - top을 pop한다.
    - top의 인덱스를 추출해 ans배열에 num을 넣는다.
    - stack이 비워지거나 top이 더 큰경우 종료
(2). 스택에 num을 넣는다.

2. 스택에 남아있는 값
    - 하나씩 pop한뒤 ans배열의 해당값의 인덱스위치에 -1을 채운다. 
'''

import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
ans = [0] * N
stack = []

# 오큰수 체크
for i in range(N):
    num = seq[i]
    # 스택이 채워져있으면서 탑이 더 작다면(뽑는경우)
    while stack and stack[-1][1] < num:
        top = stack.pop()
        ans[top[0]] = num
    stack.append([i, num])

while stack:
    top = stack.pop()
    ans[top[0]] = -1

print(*ans)