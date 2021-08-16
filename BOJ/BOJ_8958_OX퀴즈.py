# BOJ 8958 OX퀴즈

for t in range(int(input())):
  score = 0
  quiz = input()
  conti = 0
  for q in quiz:
    if q=='O':
      conti += 1
      score += conti
    else:
      conti = 0
  print(score)