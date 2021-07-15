# 병합 정렬 (Merge Sort) 다른 풀이

test = [120, 19, 18, 17, 16, 10,15,14,13,10, 12,11,9,8,7,6,5,4,3,2,1]

sort_arr = [0] * len(test)

def merge(arr, n, middle, m):
    k = n
    i = n
    j = middle + 1

    # 작은 수부터 삽입
    while i <= middle and j <= m:
        if arr[i] < arr[j]:
            sort_arr[k] = arr[i]
            i += 1
        else:
            sort_arr[k] = arr[j]
            j += 1
        k += 1
    
    # 남은 수도 넣자
    if i > middle:
        sort_arr[k:m] = arr[j:m+1]
    else:
        sort_arr[k:m] = arr[i:middle+1]
    
    # 정렬된 리스트를 다시 arr에 넣는다.
    arr[n:m+1] = sort_arr[n:m+1]

def mergeSort(arr, n, m):
    if n < m:   # 길이가 1 이상이면
        middle = (n + m) // 2
        mergeSort(arr, n, middle)
        mergeSort(arr, middle+1, m)
        merge(arr, n, middle, m)

mergeSort(test, 0, len(test) - 1)

import sys
sys.stdout.write(" ".join(map(str, test)))



