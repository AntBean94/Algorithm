# BOJ 2750 수 정렬하기

# 퀵 정렬로 풀기
arr = list(map(int, input().split()))

def QuickSort(arr, start, end):
    if start >= end:
        return
    
    key = start
    i = start + 1
    j = end

    while i <= j:
        while i < (end + 1) and arr[i] <= arr[key]:
            i += 1
        while j > start and arr[j] >= arr[key]:
            j -= 1

        if i > j:
            arr[key], arr[j] = arr[j], arr[key]
        else:
            arr[i], arr[j] = arr[j], arr[i]

        
    QuickSort(arr, start, j - 1)
    QuickSort(arr, j + 1, end)

QuickSort(arr, 0, len(arr) - 1)

print(*arr)