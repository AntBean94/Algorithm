# BOJ 2293 동전 1

'''
1. 사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우
2. 동전 중복 사용 가능
'''
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
T = [0] * (K + 1)
T[0] = 1
for _ in range(N):
    n = int(input())
    for i in range(K):
        if i + n > K: continue
        T[i + n] += T[i]
print(T[-1])