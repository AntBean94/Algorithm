# BOJ 1557 제곱 ㄴㄴ

'''
아이디어

1. K 번째 제곱 ㄴㄴ수 구하기
- K + a(제곱ㄴㄴ수 이하의 제곱수의 갯수)
ex) K = 13 일 때
19 = 13 + 6(4, 8, 9, 12, 16, 18)

2. 제곱이 포함되는 수의 갯수 세기: a
- 포함-배제 원리
(포함-배제 원리, inclusion-exclusion principle)
조합론에서 여러 개의 합집합의 크기를 구할 때 사용하는 공식.
대표적인 예시로 |AUB| = |A| + |B| - |A∩B|
위의 예시를 일반화한 식이 포함-배제 원리이다.

ex) 20이하의 자연수 중 제곱수의 갯수를 구하기
A2: 2의 제곱수
A3: 3의 제곱수

A2: 4, 8, 12, 16 ...
A3: 9, 18 ...

=> 4 + 2 - 0 = 6

40이하라면? (소수의 제곱수의 배수)
A2: 4, 8, 12, 16, 20, 24, 28, 32, 36, 40 = 10개
A3: 9, 18, 27, 36 = 4개
A5: 25 = 1개

10 + 4 + 1 - 1 - 0 - 0 + 0 = 14개

교집합의 갯수 = N // 제곱수간의 곱 (즉, 제곱수의 배수)

A2: 4
A3: 9
A5: 25
A7: 49
A11: 121
A13: 169
A17: 289
A19: 361
A23: 529
A29: 841
A31: 961
A37: 1369
:
:
A31623(근방의 소수): 약 10억

적절한 N을 어떻게 결정할지? => 이분탐색 활용

프로세스
1. 임의의 N값 결정
2. N보다 작은 제곱수 숫자 측정(a)
3. N - a = K번 째 제곱수
4. N - a와 K가 일치하는지 확인
5. 다르다면 이분탐색으로 범위 조정(더 작다면 s범위 축소, 더 크다면 e범위 축소)

예외처리

3번째
4 - 1 = 3
3 - 0 = 3
'''
K = int(input())
# 소수의 제곱수 배열
def get_prime(n):
    if n < 2:
        return []
    n += 1
    save = [1] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if save[i // 2]:
            k = i * i
            save[k // 2::i] = [0] * ((n - k - 1) // (2 * i) + 1)
    return [2] + [(2 * i + 1) for i in range(1, n // 2) if save[i]]
arr = get_prime(45000)
A = [i ** 2 for i in arr]
# print(len(A))
L = len(A)

# 임의의 N값 결정
s = K
e = 2000000000
result = 0
# 이분탐색
while True:
    if s == e: break
    # 임의의 N 결정
    n = (s + e) // 2
    # N에 따른 a갯수 확인(포함-배제 원리)
    a = 0
    for i in range(L):
        if A[i] > n: break
        a += n // A[i]
        for j in range(i+1, L):
            if A[i] * A[j] > n: break
            a -= n // (A[i] * A[j])
            for l in range(j+1, L):
                if A[i] * A[j] * A[l] > n: break
                a += n // (A[i] * A[j] * A[l])
                for m in range(l+1, L):
                    if A[i] * A[j] * A[l] * A[m] > n: break
                    a -= n // (A[i] * A[j] * A[l] * A[m])
                    for y in range(m+1, L):
                        if A[i] * A[j] * A[l] * A[m] * A[y] > n: break
                        a += n // (A[i] * A[j] * A[l] * A[m] * A[y])
                        for x in range(y+1, L):
                            if A[i] * A[j] * A[l] * A[m] * A[y] * A[x] > n: break
                            a -= n // (A[i] * A[j] * A[l] * A[m] * A[y] * A[x])
    
    # N이 K번째 제곱 ㄴㄴ수인지 확인(범위 조정)
    if n - a == K: 
        result = n
        break
    elif n - a > K: e = n
    else: s = n

# result값보다 작으면서 가장 큰 제곱 ㄴㄴ수를 찾는다.
ans = 0
for i in range(result, -1, -1):
    check = True
    for j in A:
        if j > i: break
        if not i % j:
            check = False
            break
    if check:
        ans = i
        break
print(ans)