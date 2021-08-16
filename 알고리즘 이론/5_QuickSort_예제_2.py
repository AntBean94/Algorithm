# 퀵 정렬(Quick Sort) 예제 (다른 풀이)

import sys

arr = [120, 19, 18, 17, 16, 10,15,14,13,10, 12,11,9,8,7,6,5,4,3,2,1]

def QuickSort(arr, start, end):
    if start >= end:    # 원소가 하나인경우 리턴
        return
    key = start
    i = start + 1
    j = end

    while i < j:    # 엇갈릴 때까지 실행
        while i < len(arr) and arr[i] <= arr[key]:   # 큰 값 탐색
            i += 1
        while j > start and arr[j] >= arr[key]:   # 작은 값 탐색
            j -= 1
        if i > j:   # 엇갈린 경우 키값과 작은 값을 교체
            arr[key], arr[j] = arr[j], arr[key]
            break
        else:   # 그렇지 않은 경우 상호 교환
            arr[i], arr[j] = arr[j], arr[i]
    
    QuickSort(arr, start, j - 1)
    QuickSort(arr, j + 1, end)
    return

QuickSort(arr, 0, len(arr) - 1)
sys.stdout.write(" ".join(map(str, arr)))