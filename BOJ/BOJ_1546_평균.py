# BOJ 1546 평균

N = int(input())
arr = list(map(int, input().split()))
maxNum = 0
for a in arr:
  if a > maxNum:
    maxNum = a
for i in range(N):
  arr[i] = arr[i] / maxNum * 100
total = 0
for j in arr:
  total += j
print(total / N)
