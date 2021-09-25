# BOJ 1676 팩토리얼 0의 개수

'''
2, 5의 쌍이 몇개 포함되는지 확인하면 됨
'''

N = int(input())
pair = [0, 0]
for i in range(2, N + 1):
    n = i
    while not n % 5:
        pair[1] += 1
        n /= 5
    while not n % 2:
        pair[0] += 1
        n /= 2
    
print(min(pair))