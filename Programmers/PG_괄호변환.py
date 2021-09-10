# Programmers 괄호 변환

def solution(p):
    def is_correct(u):
        stack = []
        for i in u:
            if not stack:
                stack.append(i)
            else:
                if i == ")" and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(i)
        if stack: return False
        else: return True

    def is_balance(u):
        cnt = [0, 0]
        for i in u:
            if i == '(': cnt[0] += 1
            else: cnt[1] += 1
        if cnt[0] == cnt[1]: return True
        else: return False

    def separate(w):
        for i in range(2, len(w) + 1, 2):
            if is_balance(w[:i]):
                return [w[:i], w[i:]]

    def reverse(v):
        nv = ''
        for i in v:
            if i == "(": nv += ")"
            else: nv += "("
        return nv

    def recur(w):
        # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환
        if w == "":
            return ""
        # 2. 문자열 w를 두 균형잡힌 괄호 문자열로 분리
        u, v = separate(w)
        # 3. 문자열 u가 "올바른 괄호 문자열"이라면 v에 대해 1단계부터 다시 수행
        if is_correct(u):
            # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환
            return u + recur(v)
        # 4. 문자열 u가 "올바른 괄호 문자열"이 아니면 다음을 수행
        else:
            # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙인다.
            result = '('
            # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과를 이어 붙인다.
            result += recur(v)
            # 4-3. ')'를 다시 붙인다.
            result += ')'
            # 4-4. u의 첫, 마지막 문자를 제거하고 나머지 문자의 괄호방향을 뒤집어 뒤에 붙인다.
            result += reverse(u[1:-1])
            # 4-5. 생성된 문자열 반환
            return result

    answer = recur(p)
    return answer



test_case = [
    "(()())()",
    ")(",
    "()))((()",
    ""
]
for tc in test_case:
    print('정답', solution(tc))