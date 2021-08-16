# BOJ 5557 1학년

'''
100 * 20 * 2 = 4000번 연산

dp?
+, - 만 가능
[0, 1, 2, 3, ..., 20]

[0, 1, 0, ..., 0]
[1, 0, 1, ..., 0]
[0, 2, 0, 1.., 0]
    :
    :
    :
    쭉 계산

'''

import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

# 저장 배열
table = [[0] * 21 for _ in range(N-1)]

# 1. 초기값 저장
table[0][num[0]] = 1
# 2. 숫자를 하나씩 순회하면서 통과
for i in range(1, N-1):
    val = num[i]
    # 2-1. 21개의 칸 검사(이전)
    for j in range(21):
        pre_freq = table[i-1][j]
        # 수가 있다면 그 수에 +, -
        if pre_freq:
            p_val = j + val
            if -1 < p_val < 21:
                # 누적
                table[i][p_val] += pre_freq
            m_val = j - val
            if -1 < m_val < 21:
                table[i][m_val] += pre_freq
print(table[N-2][num[N-1]])
