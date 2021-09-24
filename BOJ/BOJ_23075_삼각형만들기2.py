# BOJ 23075 삼각형만들기 2

'''
수열의 일반항
계차수열의 일반항을 구하면 된다.
단, 계차수열이 이중 등차를 가지고 있음
'''

from math import ceil
def cal(t):
    if t > 3 and not t % 2: t -= 3
    n = t // 6
    k = t % 6
    a, b1, b2 = 0, 0, 0
    if k == 1: a, b1, b2 = 0, 2, 3 
    elif k == 3: a, b1, b2 = 1, 2, 4
    elif k == 5: a, b1, b2 = 1, 3, 4
    n1, n2 = ceil(n/2), int(n/2)
    return a + n1*(2*b1+3*(n1-1))//2 + n2*(2*b2+3*(n2-1))//2
print(cal(int(input())))