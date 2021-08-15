# 25강 KMP(Knuth-Morris-Pratt) 문자열 알고리즘 예제

'''
예제

ababacabacaabacaaba
abacaaba

'''

# 초기값 설정
parent = input()
pattern = input()
parent_size = len(parent)
pattern_size = len(pattern)
fail_table = [0] * (pattern_size)

# 실패함수
def failFunc(pattern):
    cnt = 0
    j = 0
    for i in range(1, pattern_size):
        if pattern[i] == pattern[j]:
            cnt += 1
            j += 1
        else:
            cnt = 0
            j = 0
            if pattern[j] == pattern[i]:
                cnt += 1
                j += 1
        fail_table[i] = cnt
# 실패함수 실행
failFunc(pattern)

# 문자열 매칭 함수
def kmpMatching(parent, pattern):
    ans = []
    j = 0
    for i in range(parent_size):
        if parent[i] == pattern[j]:
            j += 1
        else:
            j = fail_table[j]
            if parent[i] == pattern[j]:
                j += 1
        if j == pattern_size:
            ans.append(i - j + 1)
            j = fail_table[j - 1]
    return ans

# KMP 문자열 매칭 함수 실행
print(kmpMatching(parent, pattern))
