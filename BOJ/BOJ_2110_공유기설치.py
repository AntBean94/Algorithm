# BOJ 2110 공유기 설치

import sys
input = sys.stdin.readline

N, C = map(int, input().split())

arr = [int(input()) for _ in range(N)]
arr.sort()

def check(k):
    result = 0
    pre = -10000000000
    for i in arr:
        if i - pre > k:
            result += 1
            pre = i
    return result

def binary(s, e):
    if s == e:
        print(s)
        return 
    m = (s + e) // 2
    if check(m) >= C:
        binary(m + 1, e)
    else:
        binary(s, m)

binary(0, 1000000001)
    

