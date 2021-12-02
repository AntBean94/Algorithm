# BOJ 6064 카잉 달력

'''
M:N 이 주어지면
x:y 가 몇 번째 해를 나타내는지?
'''

import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    M, N, x, y = map(int, input().split())
    # M으로 나눈 나머지가 x인 수의 집합
    m_set = set(i for i in range(x, M * N + 1, M))
    # N으로 나눈 나머지가 y인 수의 집합
    ans = -1
    for i in range(y, M * N + 1, N):
        if i in m_set: 
            ans = i
            break
    print(ans)