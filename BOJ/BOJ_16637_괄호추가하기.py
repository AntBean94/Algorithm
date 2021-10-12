# BOJ 16637 괄호 추가하기

'''
숫자는 최대 10개

괄호는 최대 4개

1 2 3 4 5 6 7 8 9 10

연산자를 기준으로 좌우의 수를 매칭

재귀함수
괄호 열었으면 무조건 닫혀야함 => 체크 포인트

모든 경우의 수 탐색

괄호가 열렸을 경우 바로 연산하지 않고 중간값을 넘긴다

그렇지 않을 경우 바로 연산한다음 다음 경우의 수로 넘어간다

'''

N = int(input())
line = input()
S = int(line[0])
ans = -10000000000

def cal(op, a, b):
    a, b = int(a), int(b)
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b

# 수식, 현재값, 인덱스, 괄호 열림여부
def recur(nums, n, k, p):
    global ans
    # 종료 조건
    if k == N // 2 + 1:
        # 최댓값 갱신
        if n > ans and not p: ans = n 
        return
    
    # 괄호 여부에 따른 조건 분기
    # 열려있지 않은 경우
    if not p:
        for i in range(2):
            # 안열기
            if not i:
                op = nums[2*k-1]
                num = int(nums[2*k])
                new_n = cal(op, n, num)
                recur(nums, new_n, k + 1, i)
            # 열기
            else:
                recur(nums, n, k + 1, i)
    # 열린 경우
    else:
        # 이전 수까지 연산
        pre_op = nums[2*(k-1)-1]
        pre_num = nums[2*(k-1)]
        op = nums[2*k-1]
        num = nums[2*k]
        now_n = cal(op, pre_num, num)
        new_n = cal(pre_op, n, now_n)
        # 연산 후 다시 닫는다.
        recur(nums, new_n, k + 1, 0)

recur(line, S, 1, 0)
print(ans)