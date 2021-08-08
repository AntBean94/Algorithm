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

# 1. 경우의 수 테이블 제작

# 2. 경우의 수를 적립

# 3. 문자열을 하나씩 만든다.
    # 3-1. a 가능한지 체크
    # 열을 하나뺀 테이블의 가장 높은 수가 가능한지

    # 가능하다면 a 하나빼고 다시 함수 호출

    # 불가능하다면 순서 = 순서 - a케이스
    # z 하나빼고 다시 함수 호출

    

