# 31 Prefix Sum (부분합 빠르게 구하기) 예제

'''
구간 합 빠르게 계산하기

1. Prefix Sum을 계산해 배열에 저장
2. 매 M개의 쿼리 정보를 확인할 때, 구간 합은 P[R] - P[L-1] 이다.

예제
다음과 같이 배열이 주어졌을 때 특정 구간의 합을 구하시오.
5
10 20 30 40 50

2 3 -> 50
3 4 -> 70

조건) 시간복잡도 O(N)
'''

N = int(input())
arr = list(map(int, input().split()))

P = [0] * (N + 1)
for i in range(1, N + 1):
    P[i] = P[i-1] + arr[i-1]
print(P[1:])

L, R = map(int, input().split())
sub_sum = P[R] - P[L - 1]
print(sub_sum)