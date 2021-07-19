# BOJ 단어 정렬

import sys

def chk(a, b):
    # 큰 값과 작은 값 대소비교
    # a가 b보다 크면 True반환
    # 반대는 False 반환
    i = 0
    while True:
        if ord(a[i]) == ord(b[i]):
            i += 1
        elif ord(a[i]) < ord(b[i]):
            return True
        else:
            return False 

def QuickSort(arr, start, end):
    # 퀵 정렬
    key = start
    i = start + 1
    j = end
    while i < j:
        while chk(arr[key], arr[i]):    # key값보다 크면 중단
            i += 1
        while chk(arr[j], arr[key]):    # key값보다 작으면 중단
            j -= 1
        # 엇갈린다면 j와 key값을 바꾼뒤 분할정복
        if i >= j:
            arr[j], arr[key] = arr[key], arr[j]
            key = j
        # 엇갈리지 않았다면 큰수와 작은수를 바꾸고 반복수행
        else:
            arr[i], arr[j] = arr[j], arr[i]
    # 정렬이 완료되었다면 분할 정복
    QuickSort(arr, start, j-1)
    QuickSort(arr, j+1, end)
    

N = int(input())
arr = [list() for _ in range(50)]

for _ in range(N):
    char = sys.stdin.readline().rstrip()
    arr[len(char)-1].append(char)

for i in range(50):
    lth = len(arr[i]-1)
    if lth:
        QuickSort(arr[i], 0, lth-1)
print(arr)
