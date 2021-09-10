# Programmers 문자열 압축

def solution(s):
    answer = 100000000
    lth = len(s)
    # 간격
    for d in range(1, lth//2+2):
        result = ""
        pre = ""
        cnt = 1
        for l in range(0, lth, d):
            sub = s[l:l + d]
            if pre == sub:
                cnt += 1
            else:
                if cnt == 1:
                    result += f'{pre}'
                    pre = sub
                else:
                    result += f'{cnt}{pre}'
                    cnt = 1
                    pre = sub
        if cnt > 1: result += f'{cnt}{pre}'
        else: result += f'{pre}'
        
        if len(result) < answer:
            answer = len(result)

    return answer



test_case = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd"
]
for tc in test_case:
    print(solution(tc))