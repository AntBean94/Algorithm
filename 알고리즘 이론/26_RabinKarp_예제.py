# 26강 라빈 카프 (Rabin-Karp) 문자열 매칭 알고리즘 예제

'''
예제

ababacabacaabacaaba
abacaaba

'''

P = input()
S = input()
P_size = len(P)
S_size = len(S)
P_hash = 0
S_hash = 0
ans = []

# 초기 해시값 계산
cnt = S_size - 1
for i in range(S_size):
    P_hash += ord(P[i]) * (2 ** cnt)
    S_hash += ord(S[i]) * (2 ** cnt)
    cnt -= 1

# 초기 해시값 비교
if P_hash == S_hash:
    if P[:S_size] == S:
        ans.append(0)

# 문자열 비교
for i in range(P_size - S_size):
    # 해시값 변경
    P_hash = 2 * (P_hash - ord(P[i]) * (2 ** (S_size - 1))) + ord(P[i + S_size])
    # 해시값이 같다면 문자열 비교
    if P_hash == S_hash:
        for j in range(S_size):
            if P[i + j + 1] != S[j]:
                break
            if j == S_size - 1:
                ans.append(i + 1)

print(ans)