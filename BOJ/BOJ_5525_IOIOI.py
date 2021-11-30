# BOJ 5525 IOIOI

'''
스택에 하나씩 넣으면서 길이를 만족하면
정답에 1을 더하고 
조건을 만족하지 않으면 전부 뺀다.

무조건 I로 시작
숫자만 기록?

I일때 False라면 +1, True
O일때 True라면 +1, False

I가 연속으로 나온경우 1로 초기화
O가 연속으로 나온경우 0로 초기화
'''

N = int(input())
M = int(input())
S = input()

io_lth = N * 2 + 1
ans = 0
lth = 0
check = True
for i in range(M):
    c = S[i]
    # 앞의 문자와 서로 다른 경우
    if c == "I" and not check:
        lth += 1
        check = True
    elif c == "O" and check:
        lth += 1
        check = False
    elif c == "I" and check:
        lth = 1
        check = True
    else:
        lth = 0
        check = False
    if lth == io_lth:
        ans += 1
        lth -= 2
print(ans)