# 24강 단순 문자열 매칭 (String Matching) 예제

'''
예제

Hello World!
Wor

'''

parent = input()
pattern = input()

def matching(parent, pattern):
    parent_size = len(parent)
    pattern_size = len(pattern)
    for i in range(parent_size - pattern_size):
        result = i
        for j in range(pattern_size):
            if parent[i + j] != pattern[j]:
                result = -1
                break
        if result > -1:
            return result
    return -1

result = matching(parent, pattern)
if result > -1:
    print("{}번째에서 매칭되었습니다.".format(result))
else:
    print("매칭되지 않았습니다.")