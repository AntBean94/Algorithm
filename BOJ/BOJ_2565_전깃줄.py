# BOJ 2565 전깃줄

'''
LIS 응용

매칭된 전깃줄이 증가하는 수열이면 서로 겹치지 않는다.
따라서, 없애야 하는 전깃줄의 최소 갯수 
= 전체 전깃줄 - 가장 긴 증가하는 부분 수열
'''

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
table = [0] * (501)
for i in range(1, N + 1):
    for j in range(arr[i-1][1]):
        if table[j] + 1 > table[arr[i-1][1]]:
            table[arr[i-1][1]] = table[j] + 1
print(N - max(table))
    