# 탐욕 알고리즘 (Greedy Algorithm) 예제

'''
동전 문제
500, 100, 50, 10원 동전의 갯수를
가장 적게 사용해서 금액을 지불해보자.
'''

N = int(input())
result = 0
result += N // 500
N %= 500
result += N // 100
N %= 100
result += N // 50
N %= 50
result += N // 10
print(result)