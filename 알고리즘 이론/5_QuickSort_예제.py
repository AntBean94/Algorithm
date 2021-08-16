# 퀵 정렬(Quick Sort) 예제

import sys

arr = [1, 10, 9, 8, 7, 6, 5, 4, 3, 2]

def QuickSort(arr):
    # 길이가 1이면 리턴
    if len(arr) <= 1:
        return arr
    # 피봇값 설정
    pvt_idx = 0
    pvt = arr[pvt_idx]
    left_arr = []
    right_arr = []
    while True:
        big_idx = 0
        sml_idx = 0
        # 왼쪽부터 큰 값 탐색
        for i in range(len(arr)):
            big_idx = i
            if arr[i] > pvt:
                break
        # 오른쪽부터 작은 값 탐색
        for j in range(len(arr)-1, -1, -1):
            sml_idx = j
            if arr[j] < pvt:
                break
        # 엇갈린 경우(분할 완료)
        if big_idx >= sml_idx:
            arr[pvt_idx], arr[sml_idx] = arr[sml_idx], arr[pvt_idx]
            pvt_idx = sml_idx

            # 배열을 두개로 나눠 반복
            left_arr = QuickSort(arr[:pvt_idx])
            right_arr = QuickSort(arr[pvt_idx+1:])
            break
            
        # 엇갈리지 않은 경우 교환 및 반복
        else:
            arr[sml_idx], arr[big_idx] = arr[big_idx], arr[sml_idx]

    arr = left_arr + [pvt] + right_arr
    return arr

sys.stdout.write(" ".join(map(str, QuickSort(arr))))