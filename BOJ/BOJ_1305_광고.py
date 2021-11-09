# BOJ 1305 광고

'''
abbaabba
abbaabba
 0011234

baab|aa
baab
 001
4 - 1

aaaaa
aaaaa
 1234

fhafh
 0012
5 - 2 = 3

ababababc
001234560

abaabab
001123

전체 문자열의 길이 - 실패함수 마지막 값
'''

L = int(input())
ad = input()
fail_func = [0] * L
j = 0
cnt = 0
# 실패함수
for i in range(1, L):
    while j > 0 and ad[i] != ad[j]:
        j = fail_func[j - 1]
    if ad[i] == ad[j]:
        j += 1
        fail_func[i] = j

print(L - fail_func[-1])
