# Programmers 순위 검색

'''
접근 방법

각 지원자가 포함될 수 있는 해시그룹에 점수를 모두 추가한다면
각 지원자의 경우의 수: 16
지원자의 수: 50,000
+
조합 가능한 모든 경우의 수: 108개
점수를 정렬: O(NlogN)
+
조건의 수: 100,000
각 조건에 해당하는 해시값 참조: 1
배열에서 조건을 만족하는 점수의 갯수: O(logN)

0. 조건 테이블 생성
1. 지원자 정보를 순회하며 해시값에 맞춰 배열에 점수를 추가한다.
2. 배열을 모두 정렬한다.
3. 조건에 맞는 해시 테이블을 참조
4. 해시값 배열에서 점수 조건에 맞는 값의 인덱스를 반환한다.(lower_bound)
'''

import itertools
import bisect

def solution(info, query):
    answer = []
    cdt_1 = ['cpp', 'java', 'python', '-']
    cdt_2 = ['backend', 'frontend', '-']
    cdt_3 = ['junior', 'senior', '-']
    cdt_4 = ['chicken', 'pizza', '-']
    table = {}
    # 조건 테이블 생성
    for condition in itertools.product(cdt_1, cdt_2, cdt_3, cdt_4):
        condition = "".join(condition)
        table[condition] = []
    
    # 지원자 정보 분류
    for i in info:
        lang, job, career, food, score = map(str, i.split())
        cd1, cd2, cd3, cd4 = [lang, '-'], [job, '-'], [career, '-'], [food, '-']
        for condition in itertools.product(cd1, cd2, cd3, cd4):
            condition = "".join(map(str, condition))
            table[condition].append(int(score))

    # 지원자 점수 배열 정렬
    for arr in table.values():
        arr.sort()
    
    # 조건에 맞는 해시 테이블 참조
    for case in query:
        case = case.replace(' and', "")
        case = list(map(str, case.split()))
        score = int(case[-1])
        case = "".join(case[:-1])
        result = len(table[case]) - bisect.bisect_left(table[case], score)
        answer.append(result)
        
    return answer



# 1 <= len(info) <= 50,000 | 1 <= query <= 100,000
test_case = [
    [["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
    ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]]
]
for tc in test_case:
    print(solution(tc[0], tc[1]))