# BOJ 14003 가장 긴 증가하는 부분 수열 5

'''
가장 긴 증가하는 부분 수열 5

접근 방법(이분 탐색 + 인덱스 기록)
1. 이분 탐색을 통해 최대 길이를 구한다.
2. 경로 추적
- 전체 수열을 순회
- 현재 탐색하고 있는 수가 table의 몇번째 수를 변경하는지 idx에 기록
- idx를 역으로 탐색 + 최대길이를 하나씩 줄여가며 최대 부분수열의 인덱스에 
  맞는 수를 찾는다.

'''

import bisect
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

table = []
idx = []

for i in arr:
    if not table or i > table[-1]:
        table.append(i)
        idx.append(len(table) - 1)
    else:
        j = bisect.bisect_left(table, i)
        table[j] = i
        idx.append(j)

lth = len(table)
print(lth)
seq = []
for i in range(len(idx)-1, -1, -1):
    if lth == 0: break
    if lth - 1 == idx[i]:
        seq.append(arr[i])
        lth -= 1
print(*seq[::-1])