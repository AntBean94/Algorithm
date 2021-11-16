# BOJ 5636 소수 부분 문자열

'''
다양한 소수를 처리할 때는 에라토스테네스의 체...

길이가 255를 넘지않는 숫자 문자열로 이루어져있다.

이 문제에서는 2보다 크거나 같고, 10만보다 작거나 같은 소수만 소수이다.
'''

eratos = [1] * 100000
for i in range(2, int(100000 ** (1/2))):
    if not eratos[i]: continue
    for j in range(2, 100000):
        t = i * j
        if t >= 100000:
            break
        eratos[t] = 0

check = input()
while check != "0":
    ans = 0
    l = len(check)
    for i in range(l):
        num = ""
        for j in range(5):
            if i + j >= l: continue
            num += check[i+j]
            # 소수판정
            n = int(num)
            # print(n)
            if eratos[n] and n > ans:
                ans = n
    print(ans)
    # 다음값 입력
    check = input()