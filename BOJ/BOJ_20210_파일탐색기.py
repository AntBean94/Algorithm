# BOJ 20210 파일 탐색기

'''
조건 1.
숫자 - 알파벳 대-소 순서
1,2,3,...,A,a,B,b,...

조건 2.
문자 비교중 숫자가 나오는경우 숫자를 하나로 묶어 작은 수가 앞으로 오게한다.

조건 3.
같은 값을 가지는 숫자열일 경우 앞에 따라붙는 0의 개수가 적은 것이 앞으로 온다.

-------
알파벳 대소비교는 (알파벳(소문자), 알파벳) 형태로 "조건 1"을 충족
정규표현식을 활용해서 문자와 숫자로 분리 후 숫자끼리 대소비교함으로써 "조건 2"를 충족
숫자는 (숫자, 문자열의 길이) 형태로 비교함으로써 "조건 3"을 충족
'''

import re
import sys
input = sys.stdin.readline
N = int(input())
arr = [input().rstrip() for _ in range(N)]
# 익명함수 활용(정렬 기준 세우기)
t = lambda s: [(int(t), len(t)) if t.isdigit() else tuple((i.lower(), i) for i in t) for t in re.split('(\d+)', s)]
for a in sorted(arr, key=t):
    print(a)