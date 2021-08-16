# 병합 정렬 (Merge Sort) 예제

import sys

arr = [120, 19, 18, 17, 16, 10,15,14,13,10, 12,11,9,8,7,6,5,4,3,2,1]

def MergeSort(arr):
    if len(arr) < 2:
        return arr

    key = len(arr) // 2
    arr1 = MergeSort(arr[:key])
    arr2 = MergeSort(arr[key:])
    newArr = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            newArr += [arr1[i]]
            i += 1
        else:
            newArr += [arr2[j]]
            j += 1
        if i == len(arr1):
            newArr += arr2[j:]
            break
        elif j == len(arr2):
            newArr += arr1[i:]
            break
    return newArr

sys.stdout.write(" ".join(map(str, MergeSort(arr))))




