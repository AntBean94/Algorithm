# BOJ 10809 알파벳 찾기

alphabet = 'abcdefghijklmnopqrstuvwxyz'
ans = [-1] * 26
word = input()

for i in range(len(word)):
  idx = alphabet.index(word[i])
  if ans[idx] < 0:
    ans[idx] = i

print(*ans)

