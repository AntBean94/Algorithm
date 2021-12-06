# BOJ 9625 BABBA

'''
B => BA
A => B

두개의 테이블
A = []
B = []
바텀업 방식
'''

K = int(input())
A = [0] * (K + 1)
B = [0] * (K + 1)
A[0] = 1
for i in range(1, K + 1):
    B[i] = B[i - 1] + A[i - 1]
    A[i] = B[i - 1]
print(A[K], B[K])