# Programmers 해시 전화번호 목록

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