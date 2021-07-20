# BOJ 1431 시리얼 번호

import sys

def customSum(c):
    num = 0
    for d in c:
        if ord(d) < 10:
            num += int(d)
    return num

def customSort(arr):
    
    return arr

N = int(input())
arr = [list() for _ in range(50)]
for _ in range(N):
    char = sys.stdin.readline().rstrip()
    arr[len(char)].append(char)
for i in range(50):
    arr[i] = customSort(arr[i])