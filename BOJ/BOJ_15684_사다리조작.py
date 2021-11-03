# BOJ 15684 사다리 조작

'''
접근 방법

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
배열을 타고 내려가면서 0이 아닌 숫자를 만나면 숫자에 해당하는 행으로 이동
마지막 열까지 이동시 출발점과 같은지 확인(모든 행에 대해서)

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



'''

from itertools import combinations as cb
import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())

# 1. 맵 그리기
ladder = [[0] * (H+1) for _ in range(N+1)]

for m in range(M):
    a, b = map(int, input().split())
    ladder[b][a] = b + 1
    ladder[b + 1][a] = b

ans = 100000000

def check(ladder):
    for i in range(1, N+1):
        y, x = i, 1
        for _ in range(1, H+1):
            if ladder[y][x] != 0:
                y = ladder[y][x]
            x += 1
        if y != i:
            return False
    return True

def cal_case(ladder, row, stack):
    for i in range(1, H+1):
        if not ladder[row][i]:
            # 사다리를 그릴 수 있는 행
            if row + 1 <= N and not ladder[row+1][i]:
                stack.append(i)

# 2. 탐색하기 (사다리 정보, 깊이 = 1, 선 갯수, 가능한 갯수)
def backT(ladder, r, line, k):
    global ans
    if line > k:
        return
    # 탈출 조건
    if r == N+1:
        if line < ans and check(ladder):
            ans = line
            if ans == k:
                print(ans)
                exit()
        return

    # 가능한 경우의 수 체크(stack: 가능한, e: 오른쪽 갯수)
    stack = []
    if k > line:
        cal_case(ladder, r, stack)

    # 가지를 그릴 수 있는 경우의 수(0, 1, ... , k - 라인)
    for i in range(0, k - line + 1):
        for case in cb(stack, i):
            # 그리기
            for c in case:
                ladder[r][c] = r + 1
                ladder[r+1][c] = r
                line += 1
            # 검증
            backT(ladder, r + 1, line, k)
            # 지우기
            for c in case:
                ladder[r][c] = 0
                ladder[r+1][c] = 0
                line -= 1
    return

for k in range(4):
    backT(ladder, 1, 0, k)
if ans > 3:
    print(-1)