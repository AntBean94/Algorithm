# BOJ 1992 쿼드트리

'''
분할정복 기법

1. check 함수를 통과하면 숫자를 붙인다.(압축 가능)
2. check 함수를 통과하지 못하면 괄호를 확장하고 분할한뒤 재귀호출
3. 재귀 호출이 종료되면 괄호를 닫는다.
'''

import sys
input = sys.stdin.readline

N = int(input())
vid = [list() for _ in range(N)]
for i in range(N):
    line = input().rstrip()
    for j in line:
        vid[i].append(j)

def check(arr, y, x, n):
    if n == 1: return True
    std = arr[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if arr[i][j] != std:
                return False
    return True

def compress(arr, y, x, n):
    global result
    if check(arr, y, x, n):
        result += f'{arr[y][x]}'
    else:
        result += '('
        h = n // 2
        compress(arr, y, x, h)
        compress(arr, y, x + h, h)
        compress(arr, y + h, x, h)
        compress(arr, y + h, x + h, h)
        result += ')'

result = ""
compress(vid, 0, 0, N)
print(result)