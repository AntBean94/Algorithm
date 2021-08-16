# BOJ 4673 셀프 넘버

def d(n):
  for i in str(n):
    n += int(i)
  if n > 10000:
    return
  arr[n] = 0
  return d(n)

arr = [1] * 10001

for i in range(1, 10001):
  if arr[i]:
    d(i)

for j in range(1, len(arr)):
  if arr[j]:
    print(j)