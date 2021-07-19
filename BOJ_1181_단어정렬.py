# BOJ 단어 정렬

import sys

def check_dic(a, b):
    pass

def QuickSort(arr, start, end):
    # 퀵 정렬
    i = start
    j = end

    
    return

N = int(input())
arr = [list() for _ in range(50)]

for _ in range(N):
    char = sys.stdin.readline().rstrip()
    arr[len(char)-1].append(char)

for i in range(50):
    lth = len(arr[i]-1)
    if lth:
        QuickSort(arr[i], 0, lth-1)
