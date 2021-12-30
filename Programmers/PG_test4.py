# PG test4

'''
그리디
R - G - B

R로 모두 바꿔야함

GBBG
1 BRBG
2 RGBG
3 RBRG
4 RRGG
5 RRBB
6 RRRR

그리디

배열로 관리
[G, B, B, G]

1. 첫 글자부터 진행
2. 바꿀 범위 탐색
3. 첫 번째가 무엇이냐에 따라 변경횟수 결정
4. 변경횟수에 따라 범위에 있는 모든 문자 변경
5. 다음 글자 탐색

쿼리 날려서
더하기 빼기 여부

[2, ], [], [], [, 2]

'''
def change(light, cnt):
    if cnt == 0: return light
    if light == "R":
        if cnt == 1: return "G"
        else: return "B"
    elif light == "G":
        if cnt == 1: return "B"
        else: return "R"
    else:
        if cnt == 1: return "R"
        else: return "G"

def solution(n, k, bulbs):
    answer = 0
    # greedy
    # 전구 배열로 변환
    bulbs = [i for i in bulbs]
    prefix = [[0, 0] for _ in range(n)]
    # 모든 글자 탐색
    for i in range(n - k + 1):
        # 현재 전구 확인
        cur = bulbs[i]
        # 이부분 수정해야함
        # if cur == "R": continue
        # elif cur == "B": cnt = 1
        # else: cnt = 2
        # 누적합 배열 만들기
        prefix[i][0] += cnt
        prefix[i + k - 1][1] += cnt
    
    # 문자 변경
    nums = 0
    print(bulbs)
    print(prefix)
    for i in range(n):
        nums += prefix[i][0]
        nums -= prefix[i][1]
        bulbs[i] = change(bulbs[i], nums % 3)

    print(bulbs)
    # 검증
    for i in range(n - k, n):
        if bulbs[i] is not "R": return -1
    return answer

test_case = [
    [6, 3, "RBGRGB"],
    [3, 2, "BGG"],
    [4, 2, "GBBG"]
]
for tc in test_case:
    print(solution(tc[0], tc[1], tc[2]))