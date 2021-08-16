# Programmers 해시 전화번호 목록

'''
startswith 메서드

파이썬 startswith() 메서드는 true, false를 반환하며
문자열 시작 부분에 서브 문자열 지정 여부를 확인하는데 사용된다.
대소문자를 구별한다.

문법
str.startswith(str, beg=0, end=len(string))
beg => 문자열 검색의 시작 위치를 설정하는데 사용
end => 문자열의 끝 위치를 설정하는데 사용

ex)
str = "hi my name is Kevin!"
print(str.startswith(hi)) # True
print(str.startswith(my, 3, 5)) # True
print(str.startswith(kevin, 0, 5)) # False

'''

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        now = phone_book[i]
        nxt = phone_book[i+1]
        if nxt.startswith(now):
            return False
    return True


# 예제 실행
test_case = [
    ["119", "97674223", "1195524421"],
    ["123","456","789"],
    ["12","123","1235","567","88"]
]
for tc in test_case:
    print(solution(tc))