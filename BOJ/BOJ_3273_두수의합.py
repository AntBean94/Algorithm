# BOJ 3273 두 수의 합

'''
1. 정렬
2. 양 끝에서 두개의 포인터를 사용해 가운데로 간다.
3. 두 값의 합이 조건을 만족하면 cnt += 1, 좌측 포인터를 1증가
4. 두 값의 합이 조건보다 작으면 좌측 포인터 1 증가
5. 두 값으 합이 조검보다 크면 우측 포인터 1 감소

'''

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
X = int(input())

arr.sort()
i = 0
j = N - 1
cnt = 0
while i != j:
    # 같다면
    if arr[i] + arr[j] == X:
        cnt += 1
        i += 1
    elif arr[i] + arr[j] < X:
        i += 1
    else:
        j -= 1
print(cnt)