# BOJ 2750 수 정렬하기

# 입력의 최대 갯수는 1000개
# 오름차순 정렬 후 출력

N = int(input())
nums = []
for _ in range(N):
    nums += [int(input())]

'''
정렬의 종류
- O(n^2): Bubble Sort, Selection Sort, Insertion Sort, Shell Sort, Quick Sort
- O(n log n): Heap Sort, Merge Sort
- O(kn): Radix Sort(4바이트 이하의 크기에서만 성능 발휘)
'''

# 1. 내장함수 사용하기 (timsort: nlogn)
'''
timsort = insertion + merge sort
'''
nums.sort()
for i in range(len(nums)):
    print(nums[i])

# 2. Bubble Sort
'''
인접한 두 개의 원소를 비교하여 자리를 교환하는 방식이다.
1. 첫 번째 원소부터 마지막 원소까지 반복하여 한 단계가 끝나면 가장 큰 원소가 마지막 자리로
정렬.
2. 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서, 맨 마지막 자리로 이동하는 모습이
물속에서 물 위로 올라오는 물방울 모양과 같다고 하여 버블 정렬이라고 한다.
'''