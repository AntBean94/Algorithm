# 비트 연산자를 활용한 부분집합 구하기(공집합, 진부분집합 포함)

arr = list(map(int, input().split()))

for i in range(1 << len(arr)):
    sub = ""
    for j in range(len(arr)):
        if i & (1 << j):
            sub += str(arr[j])
            sub += ' '
    print(sub)