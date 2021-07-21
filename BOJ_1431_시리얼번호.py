# BOJ 1431 시리얼 번호

import sys

N = int(input())
nums = [list(list() for _ in range(451)) for _ in range(50)]
lth_set = set()
num_set = set()
for i in range(N):
    line = sys.stdin.readline().rstrip()
    lth = len(line)
    lth_set.add(lth)
    num = 0
    for i in line:
        if ord(i) < 58:
            num += int(i)
    num_set.add(num)
    nums[lth-1][num].append(line)

lth_set = sorted(list(lth_set))
num_set = sorted(list(num_set))
for i in lth_set:
    for j in num_set:
        if nums[i-1][j]:
            nums[i-1][j].sort()

for i in lth_set:
    for j in num_set:
        sys.stdout.writelines("\n".join(nums[i-1][j]))
        if nums[i-1][j]:
            print("", end="\n")
