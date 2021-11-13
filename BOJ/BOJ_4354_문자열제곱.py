# BOJ 4354 문자열 제곱

'''
1. 
abcd = 1
0000

4 - 0 = 4
4 / 4 = 1

2. 
aaaa = 4
0123

4 - 3 = 1
4 / 1 = 4

3. 
ababab = 3
001234

6 - 4 = 2
6 / 2 = 3

단, 나누어 떨어지지 않을 경우 1 출력
'''

import sys
input = sys.stdin.readline

def fail_func(char, l):
    table = [0] * l
    j = 0
    for i in range(1, l):
        while j > 0 and char[i] != char[j]:
            j = table[j - 1]
        if char[i] == char[j]:
            j += 1
            table[i] = j
    result = l - table[-1]
    if l % result: return 1
    else: return l // result

while True:
    char = input()
    if char == ".": exit()
    L = len(char)
    ans = fail_func(char, L)
    print(ans)