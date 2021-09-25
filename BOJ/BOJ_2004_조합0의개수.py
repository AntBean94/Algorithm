# BOJ 2004 조합 0의 개수

'''
ex)
N을 5로 나눈 몫 더하기
N을 5^2로 나눈 몫 더하기
:
:

M과 (N-M)을 5로 나눈 몫 빼기
:
:

-------
N을 2로...

이렇게 갯수를 구한뒤 2, 5가 들어간 횟수의 최솟값을 출력
'''

N, M = map(int, input().split())
S = N - M
ans = [0, 0]
a, b = 5, 2
while a <= N:
    ans[0] += N // a
    ans[0] -= M // a
    ans[0] -= S // a
    a *= 5
while b <= N:
    ans[1] += N // b
    ans[1] -= M // b
    ans[1] -= S // b
    b *= 2
print(min(ans))