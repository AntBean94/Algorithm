# BOJ 12865 평범한 배낭

'''
무게, 가치

K = 8

6 13
4 8
3 6
4 7
5 12
1 4
2 7

1 4 -
2 7 -
3 6 -
4 7
4 8
6 13

20

무게 배열: 무게를 인덱스로 각 무게가 가질 수 있는 최대가치 측정?
[4, 7, 11, 10, 17, 16, 19, 20, 25, 0, 0]

15
인덱스 0부터 자기 자신을 더한 값까지
1:0,|1
4:0, 1, 0, 0,|4, 5
7:0, 1, 0, 0, 4, 5, 0,|7, 8, 0, 0, 11, 12
3:0, 1, 2,|3, 4, 5, 6, 7, 8
4:0, 1, 2, 3,|4, 5, 6, 7, 8|

수정 가능한 인덱스: 이전 인덱스중 0
0 이아닌 인덱스는 값이 0이 아닌경우만 다음수식 적용
=> i + 자신의 크기 < 버틸 수 있는무게 and table[i] + arr[k] > table[i + k]

초기화

100000

'''


import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
arr.sort()
table = [[0] * (100001) for _ in range(N + 1)]

cum = 0
for i in range(1, N + 1):
    w = arr[i][0]
    v = arr[i][1]
    if cum < K: cum += w
    else: cum = K
    # 초기값은 더할 수 있으면 더한다.
    table[i][w] = max(v, table[i - 1][w])
    # 자기보다 작은경우
    for j in range(w):
        table[i][j] = table[i - 1][j]
    # 자기보다 큰 경우
    for j in range(w + 1, cum + 1):
        # value가 0 이상인값 or 값이 변경 가능한 경우
        if table[i - 1][j - w] or table[i - 1][j]:
            table[i][j] = max(table[i - 1][j], table[i - 1][j - w] + v)
print(max(table[N][:K+1]))