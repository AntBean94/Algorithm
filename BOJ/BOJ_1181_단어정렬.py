# BOJ 단어 정렬

# 주의! python은 문자열 비교시 사전순 결과를 자동 제공

import sys

N = int(input())

arr = [list() for _ in range(50)]

for _ in range(N):
    char = sys.stdin.readline().rstrip()
    arr[len(char)-1].append(char)

for i in range(50):
    arr[i] = sorted(arr[i])
pre = ''
for i in range(50):
    lth = len(arr[i])
    if lth:
        for j in range(lth):
            if arr[i][j] != pre:
                sys.stdout.write("%s\n" %arr[i][j])
            pre = arr[i][j]
