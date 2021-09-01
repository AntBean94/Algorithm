# BOJ 1654 랜선 자르기

'''
K개를 길이로 나눠서 몫이 몇개나오는지 체크
자신보다 작은 수가 몇개 나오는지 알 수 있다.
이를 통해 길이 예측 가능 

'''

import sys
input = sys.stdin.readline

K, N = map(int, input().split())

arr = [int(input()) for _ in range(K)]

# 가능한 길이 갯수 함수
def check(k):
    result = 0
    for i in arr:
        result += i // k
    return result

# 이분 탐색 함수
def binary(s, e):
    if s == e: 
        print(s - 1)
        return
    m = (s + e) // 2
    # print(m)
    if check(m) >= N:
        binary(m + 1, e)
    else:
        binary(s, m)

binary(0, 100000000000)