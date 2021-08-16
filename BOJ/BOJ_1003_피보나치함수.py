# BOJ 1003 피보나치 함수

'''
작은문제, 큰문제
0 => 1 0
1 => 0 1

이후 d[an, bn] = d[an-1, bn-1] + d[an-2, bn-2]
'''

T = int(input())
for _ in range(T):
    N = int(input())
    d = [[0, 0] for _ in range(N+1)]
    if N==0:
        print(1, 0)
    elif N==1:
        print(0, 1)
    else:
        d[0] = [1, 0]
        d[1] = [0, 1]
        for i in range(2, N+1):
            d[i][0] = d[i-1][0] + d[i-2][0]
            d[i][1] = d[i-1][1] + d[i-2][1]
        print(*d[N])
