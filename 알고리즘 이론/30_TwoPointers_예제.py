# 30 Two Pointers (투 포인터) 예제

'''
아래와 같이 자연수로 구성된 수열이 있다.

1 2 3 2 5

이 때, 합이 5인 부분 연속 수열의 갯수를 구해보시오.

조건) 시간복잡도 O(N)
'''

M = int(input())
arr = list(map(int, input().split()))
L = len(arr)

cnt, sub_total = 0, arr[0]
start, end = 0, 0
i = 0

while start < L and end < L:
    if sub_total == M:
        cnt += 1
        end += 1
        if end < L: sub_total += arr[end]
    elif sub_total < M:
        end += 1
        if end < L: sub_total += arr[end]
    else:
        sub_total -= arr[start]
        start += 1

print(cnt)