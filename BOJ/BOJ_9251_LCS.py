# BOJ 9251 LCS (Longest Common Subsequence, 최장 공통 부분 수열)

'''
ACAYKP
CAPCAK

ACAK

문자열 두개를 순회하면서(2중 for문)
table을 채운다.

비교하는 두 문자의 값이 같으면 table(이전값) + 1
비교하는 두 문자의 값이 다르면 이전값중 더 큰값을 상속
'''


A = input()
B = input()

A_lth = len(A)
B_lth = len(B)

table = [[0] * (B_lth + 1) for _ in range(A_lth + 1)]
for i in range(1, A_lth+1):
    for j in range(1, B_lth+1):
        if A[i-1] == B[j-1]:
            table[i][j] = table[i-1][j-1] + 1
        else:
            table[i][j] = max(table[i-1][j], table[i][j-1])
print(max(table[A_lth]))
