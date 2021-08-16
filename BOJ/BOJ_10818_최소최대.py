# BOJ 10818 최소, 최대

N = int(input())
arr = list(map(int, input().split()))
minnum = 1000001
maxnum = -1000001
for i in arr:
  if i > maxnum:
    maxnum = i
  if i < minnum:
    minnum = i
print(minnum, maxnum)
