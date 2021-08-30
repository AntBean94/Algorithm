# Programmers 신규 아이디 추천
import re

def solution(new_id):
    answer = ''
    # 1단계
    answer = new_id.lower()
    # 2단계
    answer = re.sub(r"[^a-z0-9-_.]", "", answer)
    # 3단계
    pre = ""
    new = ""
    for i in range(len(answer)):
        if answer[i] == "." and pre == ".": continue
        else:
            pre = answer[i]
            new += answer[i]
    answer = new
    # 4단계
    if answer:
        if answer[0] == ".": answer = answer[1:]
    if answer:
        if answer[-1] == ".": answer = answer[:-1]
    # 5단계
    else:
        answer = "a"
    # 6단계
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    # 7단계
    while len(answer) < 3:
        answer += answer[-1]

    return answer


test_case = [
    "...!@BaT#*..y.abcdefghijklm",
    "z-+.^.",
    "=.=",
    "123_.def",
    "abcdefghijklmn.p"
]
for tc in test_case:
    print(solution(tc))