# Programmers 메뉴 리뉴얼

'''
LCS?
문자열에 존재하는 모든 조합의 수
ex) 2개라면 2로 조합이 가능한 모든 메뉴로 검사


'''

import itertools

def solution(orders, course):
    answer = []
    result = [dict() for _ in range(11)]
    for order in orders:
        order = [i for i in order]
        order.sort()
        for i in course:
            for case in itertools.combinations(order, i):
                case = "".join(case)
                if case in result[i]:
                    result[i][case] += 1
                else:
                    result[i][case] = 1
    for i in course:
        if result[i]:
            tmp = []
            cnt = 2
            for key, value in result[i].items():
                if value > cnt:
                    tmp = []
                    tmp.append(key)
                    cnt = value
                elif value == cnt:
                    tmp.append(key)
            for t in tmp:
                answer.append(t)
        
    answer.sort()
    return answer




test_case = [
    [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]],
    [["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]],
    [["XYZ", "XWY", "WXA"], [2,3,4]]
]
for orders, course in test_case:
    print('정답은: ', solution(orders, course))
    print()