# BOJ 1541 잃어버린 괄호

'''
문제
주어진 식에 괄호를 적절히 쳐서 최소값을 출력하기

조건
1. 식은 0 ~ 9, +, - 로만 구성된다
2. 가장 처음과 마지막 문자는 숫자
3. 연속해서 두개 이상의 연산자가 나타나지 않는다
4. 숫자는 100000 이하
5. 숫자는 0으로 시작가능
6. 입력되는 식의 길이는 50 이하

- 부호 이후에 모든 정수는 빼주면 된다.

'''
num = input()

ans = 0
check = True
k = ""
for i in range(len(num)):
    if num[i] == '+' or num[i] == '-':
        if check:
            ans += int(k)
        else:
            ans -= int(k)
        k = ""
    else:
        k += num[i]
    if num[i] == '-':
        check = False

if check:
    ans += int(k)
else:
    ans -= int(k)

print(ans)