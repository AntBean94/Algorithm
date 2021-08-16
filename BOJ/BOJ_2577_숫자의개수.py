# BOJ 2577 숫자의 개수

num = 1
for i in range(3):
  n = int(input())
  num *= n
num = str(num)
arr = [0] * 10
for j in num:
  arr[int(j)] += 1
for k in arr:
  print(k)
    