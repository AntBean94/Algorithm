# BOJ 10989 수 정렬하기 3

# 계수정렬 알고리즘 활용 O(N)

'''
import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [0] * 10000
for i in range(N):
    arr[int(sys.stdin.readline())-1] += 1

for i in range(10000):
    if arr[i]:
        for _ in range(arr[i]):
            sys.stdout.write(str(i+1)+"\n")
'''
from sys import stdin, stdout

stdin = open('input.txt', 'r')

stdin.readline()
cnt = [0] * 10000
for n in stdin:
    cnt[int(n)-1] += 1
for i in range(10000):
    stdout.write(f'{i+1}\n' * cnt[i])
