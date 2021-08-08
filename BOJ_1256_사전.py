# BOJ 1256 사전

''' 풀이

역 추적?

a x 1, z x 1
az
za

a x 2, z x 2
1 aazz
2 azaz
3 azza
4 zaaz
5 zaza
6 zzaa

a x 3, z x 2
aaazz
aazaz
aazza
azaaz
azaza
azzaa
zaaaz
zaaza
zazaa
zzaaa


aaa
aaz

aza
azz <=

zaa
zaz

zza
zzz

[]

경우의 수 구하는것은 문제가 안됨

(1, 0) (2, 1) (3, 3) (4, 6)
(1, 0) (1, 1) (1, 2) (1, 3)
(1, 1) (0, 1) (0, 1) (0, 1)

1 3 6 10 
1 2 3 4
1 1 1 1 

맨앞에 a를 택하면 가능한 경우의 수 : 6
=> 행을 하나 지운채로 계산하면 된다.
이 수가 K보다 작다면 z를 선택

첫 번째 경우의 수
a 선택
열 하나를 날리고 가능한 경우의 수 : 6

4번째를 구하고 싶다.
a:가능
a:불가능 => z
4 - 3
즉 1번째
a: 가능

azaaz

'''

N, M, K = map(int, input().split())
ans = ""

# 1. 경우의 수 테이블 제작
cases = [[0] * (N+1) for _ in range(M+1)]
cases[0][0] = 1

# 2. 경우의 수를 적립
for i in range(M+1):
    for j in range(N+1):
        y = i + 1
        x = j + 1
        if y < M + 1:
            cases[y][j] += cases[i][j]
        if x < N + 1:
            cases[i][x] += cases[i][j]

# 조건 체크
if cases[M][N] < K:
    ans = -1
# 3. 문자열을 하나씩 만든다.
else:
    numA, numZ = N, M
    seq = K
    while len(ans) < N + M:

        # 3-1. a 가능한지 체크
        if cases[numZ][numA - 1] >= seq:
            ans += 'a'
            numA -= 1
        else:
            seq -= cases[numZ][numA - 1]
            ans += 'z'
            numZ -= 1
        # 하나만 남은 경우 종료
        if numA == 0:
            ans += 'z' * numZ
            break
        if numZ == 0:
            ans += 'a' * numA
            break

print(ans)
