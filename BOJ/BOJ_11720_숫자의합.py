# BOJ 11720 숫자의 합

N = int(input())
num = input()
total = 0
for i in range(N):
  total += int(num[i])
print(total)