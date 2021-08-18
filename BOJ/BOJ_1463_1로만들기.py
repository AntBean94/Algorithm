# BOJ 1463 1로 만들기

N = int(input())

arr = [0] * (N + 1)
for i in range(N, 1, -1):
    if i % 3 == 0:
        if arr[i // 3] == 0:
            arr[i // 3] = arr[i] + 1
        else:
            if arr[i] + 1 < arr[i // 3]:
                arr[i // 3] = arr[i] + 1
    if i % 2 == 0:
        if arr[i // 2] == 0:
            arr[i // 2] = arr[i] + 1
        else:
            if arr[i] + 1 < arr[i // 2]:
                arr[i // 2] = arr[i] + 1
    if arr[i - 1] == 0:
        arr[i - 1] = arr[i] + 1
    else:
        if arr[i] + 1 < arr[i - 1]:
            arr[i - 1] = arr[i] + 1
print(arr[1])