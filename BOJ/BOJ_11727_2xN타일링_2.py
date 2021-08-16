# BOJ 11727 2xN 타일링 2

'''
식 추론

n =
[n-1] + |
+
[n-2] + = or ㅁ

점화식
D(n) = D(n-2) + D(n-1) * 2
'''

n = int(input())
arr = [0] * (n+1)
for i in range(n+1):
    if i < 2:
        arr[i] = 1
    else:
        arr[i] = (arr[i-1] + arr[i-2] * 2) % 10007
print(arr[n])