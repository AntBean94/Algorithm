# BOJ 1309 동물원

'''
Dynamic Programming

우측배치 | 배치 X | 좌측배치

1 1 1
2 3 2 
:
:

즉, DP[n][사자배치] = sum(DP[n-1][사자 배치X])
'''

N = int(input())
DP = [1, 1, 1]
for i in range(1, N):
    a = sum(DP[1:])
    b = sum(DP)
    c = sum(DP[:2])
    DP = [a, b, c]
print(sum(DP) % 9901)