# BOJ 2133 타일 채우기

'''
문제 
3xN 크기의 블록을 2x1, 1x2의 블록으로 채우는 경우의 수

n 
홀수의 경우 채울 수 없음: 0가지 경우의 수

짝수
||  ||=
=   =||

-2, -4
-2: 3가지 경우
-4: 2가지 경우
-6: 2가지 경우
  :
  :
  :
0이 될때까지 짝수개에는 중간에 끊을 수 없는 경우의 수 2개씩 존재


D(n) = 3xD(n-2) + 2xD(n-4) + 2xD(n-6) ... 2xD(0)

6 = 2 * (2 * 3) + 3*3*3 = 12 + 27 = 39

2 => 3

4 => 3 * 3 + 2

6 => 3 * 11 + 3*2 + 2

8 => 3 * 39 + 11*2 + 3*2 + 2
'''

n = int(input())
arr = [0] * (n+1)
sub = 0
for i in range(2, n+1, 2):
    if i == 2:
        arr[2] = 3
    elif i == 4:
        sub = 2
        arr[4] = 11
    else:
        sub += 2 * arr[i-4]
        arr[i] = 3 * arr[i-2] + sub
print(arr[n])