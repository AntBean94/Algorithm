# BOJ 1918 후위 표기식

'''
중위 표기식 => 후위 표기식
'''

idx = {"+": 1, "-": 1, "*": 2, "/": 2}
alpa = set([i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"])
infix_expr = input()
postfix_expr = ""
stack = []
for i in infix_expr:
    if i in alpa:
        postfix_expr += i
    else:
        if i == "(": stack.append(i)
        elif i == ")":
            while stack[-1] != "(":
                postfix_expr += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != "(":
                if idx[i] <= idx[stack[-1]]:
                    postfix_expr += stack.pop()
                else: break
            stack.append(i)
while stack:
    postfix_expr += stack.pop()
print(postfix_expr)