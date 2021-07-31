# BOJ 14852 타일 채우기 3

'''
문제
2xn 크기의 벽을 2x1, 1x2, 1x1 크기의 타일로 채우는 경우의 수

D(n) = 2xD(n-1) + 3xD(n-2) + 2xD(n-3) + 2xD(n-4)...+ 2xD(0)


'''

n = int(input())
arr = [0] * (n+1)
sub = 2
for i in range(1, n+1):
    if i == 1:
        arr[i] = 2
    elif i == 2:
        arr[i] = 7
    else:
        sub += 2 * arr[i - 3]
        sub %= 1000000007
        arr[i] = (3 * arr[i-2] + 2 * arr[i-1] + sub) % 1000000007

print(arr[n])