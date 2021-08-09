# BOJ 15684 사다리 조작

'''풀이
N개의 세로
M개의 가로

추가해야하는 가로선의 최소 갯수를 구하자

그래프?

엇갈리지않은 계단이 필요함 (짝수개)

예제 5번) => 불가능
|_| | | |
| |_| | |
|_| |_| |
| |_| |_|
| | |_| |
| |_| |_|
|_| | | |
| |_| | |
| | | | |

기존 선: 8개
가능한 조합 2, 4, 6, 8, ..., 


|_| |
| |_|
|_| |
| |_|
| |_|
|_| |
| |_|
|_| |
| | |
| |_|
| |_|
| | |

감싸거나, 아예 안겹치거나

|_| |
| |_|
| |_|
|_| |
| | |

[
    [2, 1, 0]
    [0, 3, 2]
    [0, 3, 2]
    [2, 1, 0]
]

스택을 활용해서 하나씩 넣었다가 뺀다음에 스택이 비어있다면 자기자신한테 가는 것

---그래프 형태---
이차원배열
N = 3
H = 5
[
    [0, 0, 2, 0, 0]
    [0, 0, 1, 3, 0]
    [0, 0, 0, 2, 0]
]

---검증 함수---
1. 라인 정보를 담는다.
- 단, 연결된 라인의 번호가 기록되어 있어야함
2. 라인을 따라 내려가면서 번호를 스택에 담는다.
3. 스택이 비어있지 않은데 번호를 추가로 만나면 스택의 첫 번째값과 비교
- 스택과 값이 같다면 스택에서 뺀다.
- 스택과 값이 다르다면 스택에 값을 추가
4. 라인을 따라 마지막까지 내려간다.
- 스택이 비어있다면 자기자신
- 스택이 차있다면 X

---조합 함수---

스택에 4개가 쌓여있다면 4개의 라인이 더 필요하다는 것



1. 그래프를 그린다.
2. 그래프를 탐색한다.
3. 행마다 검증함수에 투입
- 스택이 비어있다면 다음행 검사
- 스택이 차있다면 선을 그어야한다.
    {
        스택이 차 있다면 어디에 선을 그어야 할지 체크
            (그릴수 있는 라인 갯수 체크) = K
        - 스택이 홀수인 경우
            홀수개의 라인을 그려야한다.
            라인의 조합은 스택에 담겨있는 숫자를 각각 짝수로 만드는 조합
            1, 3, 5로 늘려간다.
            단, 그려야 하는 숫자와 스택의 숫자값이 K를 초과하면 불가능한 함수
        - 스택이 짝수인 경우
            짝수개의 라인을 그려야한다.
            라인의 조합은 스택에 담겨있는 숫자를 각각 짝수로 만드는 조합
            2, 4, 6로 늘려간다.
            단, 그려야 하는 숫자와 스택의 숫자값이 K를 초과하면 불가능한 함수
        }
    선을 그렸다면 다음 라인 호출(재귀)
    선을 그린 선을 삭제(그린 선의 정보를 담아놔야 한다.)

    탈출조건: 마지막 행을 검사한경우

검증함수 
스택이 비어있다면 비어있는 스택 반환
스택이 차있다면 

30개 선이 있다
30개 중에서 2개를 뽑는 경우의 수
30 * 29
-------
    2

만약 1, 3, 3, 3이라면
봐야하는 경우의 수
1,            3
              3, 1
3,       , 1, 


1, 3
1, 3, 3, 3
1, 1, 1, 3

****그릴 선을 정하는 방법****
그릴 선을 정하는 방법

선을 타고 내려가면서 가능한 번호를 리스트에 담는다.
[4, 5, 6]


----------------

def 함수():
if 탈출 조건:
    if 검증함수 통과:
        if 갯수가 최소라면:
            최솟값 바꾸기
    return

if 검증함수 통과:

    선은 하나만 그리면 된다!!!
    다음 라인만 보면 됨!
    즉, 가능한 라인을 검사할때는 

    stack에서 뽑아오기
    f = 첫번째 값이 몇개인지
    e = 전체는 몇개인지

    전체가 짝수이면
    if e % 2:
        s1 = 1
    else:
        s1 = 0

    for i in range(s1, 가능한 갯수, 2):
        for case in comb([], i):
            s2 = 0
            if f % 2:
                s2 = 1
            
            for k in range(s2, i+1, 2):
                t = i - k
                    
                    case 사용
                    di 사용

                    배열 그리기(case, di)

                    재귀함수
                    
                    배열 지우기(case, di)
    return
else:
    return
       
-------------------------
'''

from itertools import combinations as comb
import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())

# 1. 맵 그리기
ledder = [[0] * (H+1) for _ in range(N+1)]

for m in range(M):
    a, b = map(int, input().split())
    ledder[b][a] = b + 1
    ledder[b + 1][a] = b

ans = 100000000

def check(ledder, row):
    isP = []
    for i in ledder[row]:
        # 0이 아니면
        if i:
            # 스택이 비어있지 않다면
            if isP:
                if isP[-1] == i:
                    isP.pop(-1)
                else:
                    isP.append(i)
            # 비어있다면
            else:
                isP.append(i)
    if isP:
        return False
    else:
        return True

def cal_case(ledder, row, stack):
    cnt = 0
    for i in range(1, H+1):
        if ledder[row][i]:
            cnt += 1
        else:
            # 사다리를 그릴 수 있는 행
            if row + 1 <= N and not ledder[row+1][i]:
                stack.append(i)
    if cnt % 2:
        return 1
    else:
        return 0

# 2. 탐색하기 (사다리 정보, 깊이 = 1, 선 갯수)
def backT(ledder, r, line):
    global ans
    # 탈출 조건
    if r == N+1:
        # print('line', line)
        if line < ans:
            ans = line
            if ans == 0:
                print(ans)
                exit()
        return
    if line > 3:
        return
    # 가능한 경우의 수 체크(stack: 가능한, e: 오른쪽 갯수)
    stack = []
    s = cal_case(ledder, r, stack)
    e = len(stack)
    # print(r, stack, s, e)

    for i in range(s, 3, 2):
        for case in comb(stack, i):
            # 그리기
            # print(case)
            for c in list(case):
                ledder[r][c] = r + 1
                ledder[r+1][c] = r
                line += 1
            # 검증
            if check(ledder, r):
                # for _ in ledder:
                #     print(_)
                # print()
                backT(ledder, r + 1, line)
            # 지우기
            for c in case:
                ledder[r][c] = 0
                ledder[r+1][c] = 0
                line -= 1

# for _ in ledder:
#     print(_)
# print()
backT(ledder, 1, 0)
if ans > 3:
    print(-1)
else:
    print(ans)

