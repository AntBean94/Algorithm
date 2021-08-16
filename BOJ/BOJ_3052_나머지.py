# BOJ 3052 나머지

arr = []
for i in range(10):
  n = int(input())
  t = n % 42
  if t not in arr:
    arr.append(t)
print(len(arr))