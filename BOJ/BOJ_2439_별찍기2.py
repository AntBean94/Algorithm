# BOJ 2439 별 찍기 - 2

T = int(input())
for i in range(1, T+1):
    space = ' '*(T-i)
    star = '*'*(i)
    print(f'{space}{star}')