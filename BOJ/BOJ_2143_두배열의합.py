# BOJ 2143 두 배열의 합

'''
1. 모든 부분합을 구해둔다.
2. 각 부분합을 정렬한다.
3. 이분탐색으로 조건을 만족하는 값을 찾는다.
'''

import bisect

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
cnt = 0

def partial_sum(arr, n):
    result = {}
    for i in range(n):
        tmp = 0
        for j in range(i, n):
            tmp += arr[j]
            if tmp in result: result[tmp] += 1
            else: result[tmp] = 1       
    return result

arr1 = sorted(partial_sum(A, N).items(), key=lambda x: x)
val1 = [i[1] for i in arr1]
arr1 = [i[0] for i in arr1]
arr2 = sorted(partial_sum(B, M).items(), key=lambda x: x)
val2 = [i[1] for i in arr2]
arr2 = [i[0] for i in arr2]

arr2_len = len(arr2)
# 이분 탐색
for i in range(len(arr1)):
    k = arr1[i]
    j = bisect.bisect_left(arr2, T - k)
    if j == arr2_len: continue
    if T == k + arr2[j]: cnt += val1[i] * val2[j]
print(cnt)