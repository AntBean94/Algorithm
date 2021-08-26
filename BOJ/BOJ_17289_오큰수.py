# BOJ 17289 오큰수

'''
오큰수

3, 5, 2, 7 인 경우

스택이 비어있거나 top보다 작은수를 만나면 값을 넣는다.
top보다 큰 수를 만나면 top의 인덱스에 큰수를 넣고 top을 스택에서 꺼낸다.
- 큰 수보다 더 큰수를 만나기 전까지 반복
배열의 끝까지 체크했다면 스택에서 하나씩 뽑아 해당 위치는 -1로 채운다.
앙 기모레이~
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