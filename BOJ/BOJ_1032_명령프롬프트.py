# BOJ 1032 명령 프롬프트

N = int(input())
pattern = input()
L = len(pattern)
for i in range(N - 1):
    char = input()
    # 비교 및 재조립
    for j in range(L):
        if pattern[j] != char[j] and pattern[j] != "?":
            pattern = pattern[:j] + "?" + pattern[j+1:]
print(pattern)