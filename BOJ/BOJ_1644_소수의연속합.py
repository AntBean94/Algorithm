# BOJ 1644 소수의 연속합

'''
1. N 이하의 소수 배열 생성
2. 누적합 배열 생성
3. 투 포인터로 오른쪽으로 이동하며 구간합이 N인 지점을 찾는다.
- N이 소수면 경우의 수에 N도 포함됨

'''
import math
N = int(input())

def prime(n):
    n += 1
    save = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if save[i // 2]:
            k = i * i
            save[k // 2::i] = [False] * ((n - k - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if save[i]]

primes = prime(N)
new_arr = [0]
pre = 0
for a in primes:
    pre += a
    new_arr.append(pre)

# 투포인터로 합 찾기
cnt = 0
lth = len(new_arr)
i, j = 0, 1
while i < j and j < lth:
    l, r = new_arr[i], new_arr[j]
    sub_sum = r - l
    if sub_sum == N:
        cnt += 1
        j += 1
    elif sub_sum < N: j += 1
    else: i += 1
print(cnt)