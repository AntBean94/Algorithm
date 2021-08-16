# BOJ 1411 비슷한 단어

# 숌스럽게 바꾸기!

# 쌍이 될 수 없는 경우

N = int(input())
box = []
for i in range(N):
  box.append(input())

code_list = []
code = ''
check_list = []
for char in box:
  for i in range(len(char)):
    # 앞에서 나왔다면
    if char[i] in check_list:
      co = check_list.index(char[i])
      code += str(co)
    # 나오지 않았다면
    else:
      code += str(len(check_list))
      check_list.append(char[i])
  code_list.append(code)
  code = ''
  check_list = []

lth = len(code_list)

cnt = 0
for i in range(lth):
  for j in range(lth):
    if i!=j and code_list[i]==code_list[j]:
      cnt += 1

print(cnt//2)

