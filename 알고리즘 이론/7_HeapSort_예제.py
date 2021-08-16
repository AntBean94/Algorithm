# 힙 정렬 (Heap Sort) 예제

import sys

heap = [7, 6, 5, 8, 3, 5, 9, 1, 6]

def HeapSort(heap):
    num = len(heap)
    # 1. 최대 힙 구조 생성
    for i in range(1, num):
        j = i
        while j != 0: 
            root = (j - 1) // 2
            if heap[root] < heap[j]:
                heap[root], heap[j] = heap[j], heap[root]
            j = root
    # 2, 3 반복
    for i in range(num-1, -1, -1):
        # 2. root노드와 가장 마지막 수를 교환
        heap[0], heap[i] = heap[i], heap[0]
        # 3. heapify
        root = 0
        c = 1
        while c < i:
            c = root * 2 + 1
            if c < i - 1 and heap[c] < heap[c+1]:
                c += 1
            # 루트보다 자식이 더 크면 교환
            if c < i and heap[c] > heap[root]:
                heap[c], heap[root] = heap[root], heap[c]
            root = c

HeapSort(heap)
sys.stdout.write(" ".join(map(str, heap)))
        

