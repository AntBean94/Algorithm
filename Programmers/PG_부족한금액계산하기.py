# Programmers 부족한 금액 계산하기

def solution(price, money, count):
    total = price * (count + 1) * (count / 2)
    result = int(total - money)
    if result >= 0: answer = result
    else: answer = 0
    return answer