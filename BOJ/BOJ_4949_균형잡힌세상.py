# BOJ 4949 균형잡힌 세상

import sys
input = sys.stdin.readline

while True:
    result = 'yes'
    char = input().rstrip()
    if len(char) == 1 and char == '.': break
    stack = []
    for c in char:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')' or c == ']':
            if not stack:
                result = 'no'
                break
            if c == ')':
                if stack[-1] != '(':
                    result = 'no'
                    break
                else: stack.pop()
            elif c == ']':
                if stack[-1] != '[':
                    result = 'no'
                    break
                else: stack.pop()
    if stack: result = 'no'
    print(result)