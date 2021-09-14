# BOJ 15650 N과 M (2)

import sys
from itertools import combinations

N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
for case in combinations(arr, M):
    sys.stdout.writelines(" ".join(map(str, case)) + '\n')