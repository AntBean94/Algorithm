# BOJ 15552 빠른 A+B
# BOJ 입출력 스트림과 관련된 문제

# 중요!
# input, print 보다 sys.stdin.readline, sys.stdin.wrieline이 훨씬 빠르다.

import sys

for _ in range(int(input())):
    A, B = sys.stdin.readline().split()
    print(int(A)+int(B))
    