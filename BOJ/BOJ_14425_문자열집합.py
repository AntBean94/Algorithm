# BOJ 14425 문자열 집합

'''
집합
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
whole_set = set()
for i in range(N):
    whole_set.add(input().rstrip())
cnt = 0
for i in range(M):
    string = input().rstrip()
    if string in whole_set:
        cnt += 1
print(cnt)