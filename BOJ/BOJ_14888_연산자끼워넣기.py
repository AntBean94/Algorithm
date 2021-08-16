# BOJ 14888 연산자 끼워넣기

import sys
import itertools
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
oprs = list(map(int, input().split()))

cals = []
for i in range(len(oprs)):
    cals += [i] * oprs[i]
max_val = -1000000000
min_val = 1000000000

for cal in set(itertools.permutations(cals, N-1)):
    value = nums[0]
    k = 1
    for i in cal:
        # 덧셈
        if i == 0:
            value += nums[k]
        # 뺄셈
        elif i == 1:
            value -= nums[k]
        # 곱셈
        elif i == 2:
            value *= nums[k]
        else:
            if value < 0:
                value = - (abs(value) // nums[k])
            else:
                value //= nums[k]
        k += 1
    if value > max_val:
        max_val = value
    if value < min_val:
        min_val = value
print(max_val)
print(min_val)


