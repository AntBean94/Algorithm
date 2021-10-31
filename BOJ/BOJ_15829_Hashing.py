# BOJ 15829 Hashing

N = int(input())
char = input()
key = 0
for i in range(N):
    key += (ord(char[i]) - 96) * 31 ** i
print(key % 1234567891)