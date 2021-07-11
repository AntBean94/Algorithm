# 선택정렬(selection sort) 예제

arr = [1, 4, 3, 6, 7, 5, 2, 9, 8]

for i in range(len(arr)):
    num = i
    for j in range(i, len(arr)):
        if arr[j] < arr[num]:
            num = j
    arr[i], arr[num] = arr[num], arr[i]


print(arr)