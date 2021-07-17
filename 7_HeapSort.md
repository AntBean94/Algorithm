# 7강 힙 정렬

## Heap Sort

## 힙(Heap)을 이용해 데이터 정렬하기

---

1. 최대 힙 구조 생성
   - 전체 배열 길이의 절반만 탐색하면 됨(끝 가지 제외)
   - 아래에 가지가 있는 노드 기준으로 상향식 heapify 수행
   - 반복문으로도 가능 (루트 인덱스가 노드를 2로 나눈 몫임을 이용)
2. 가장 큰 수(힙의 최상단)와 가장 마지막 수를 교환
   - 루트 노드와 마지막 노드를 교환
   - 배열의 범위를 1 줄인다.
3. 정점을 기준으로 heapify algorithm(힙 생성 알고리즘) 수행
   - 상향식, 하향식 상관없음
   - 하향식으로 자신의 가지중 가장 큰수와 교환
4. (2, 3) 과정 반복

---

**Python**

```python
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
        j = 0
        while j < i:
            branch = j * 2 + 2
            check = True
            if branch - 1 >= i:
                break
            elif branch >= i:
                branch -= 1
                check = False
            
            # 가지 두개
            if check:
                if heap[branch - 1] > heap[branch]:
                    branch -= 1
                if heap[branch] > heap[j]:
                    heap[j], heap[branch] = heap[branch], heap[j]
            else:
                # print(branch, j, i)
                if heap[branch] > heap[j]:
                    heap[j], heap[branch] = heap[branch], heap[j]
            j = branch
HeapSort(heap)
sys.stdout.write(" ".join(map(str, heap)))
```



**C++**

```C++
#include <stdio.h>

int number = 9;
int heap[9] = {7, 6, 5, 8, 3, 5, 9, 1, 6};

int main(void) {
  // 먼저 전체 트리 구조를 최대 힙 구조로 바꾼다.
  for(int i = 1; i < number; i++) {
    int c = i;
    do {
      int root = (c - 1) / 2;
      if(heap[root] < heap[c]) {
        int temp = heap[root];
        heap[root] = heap[c];
        heap[c] = temp;
      } 
      c = root;
    } while (c != 0);
  }
  // 크기를 줄여가며 반복적으로 힙을 구성
  for(int i = number-1; i >= 0; i--) {
    int temp = heap[0];
    heap[0] = heap[i];
    heap[i] = temp;
    
    int root = 0;
    int c = 1;
    do {
      c = root * 2 + 1;
      if(heap[c] < heap[c + 1] && c < i - 1) {
        c++;
      }
      // 루트보다 자식이 더 크다면 교환
      if(heap[c] > heap[root] && c < i) {
        int temp = heap[c];
        heap[c] = heap[root];
        heap[root] = heap[c];
      }
      root = c;
    } while (c < i);
  }
  for(int i = 0; i < number; i++) {
    printf("%d ", heap[i]);
  }
}
```



**Python v.2**

```python
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
```



## 효율성

1. 최대힙 구성 ... N

   ```markdown
   트리구조에서 힙을 구성하는데는 시간복잡도 O(N)이 소모된다.
   
   트리구조의 높이는 logN (8~15개면 3층, 16~31개면 4층...)
   
   트리구조의 가장 밑에있는 가지마다(1/2 * N) 상향식 정렬(logN)을 수행하므로
   
   시간복잡도는 1/2 * N * logN
   
   => logN이 1/2 * N 보다 작으므로 
   
   1/2 * N * logN <= N
   
   => 따라서 시간복잡도는 N
   ```

2. 정점의 수를 정렬 ... N * logN

   ```
   수를 한개씩 정렬 ... N
   
   각 수를 정렬할 때마다 힙 생성 알고리즘(logN) 반복
   
   따라서 N logN
   ```



> 힙 정렬은 병합 정렬과 다르게 별도로 추가적인 배열을 생성하지 않아도 되기 때문에 **메모리 측면에서 매우 효율적**이다. 또한 항상 N*logN 의 시간복잡도를 보장할 수 있기 때문에 이론적으로 병합정렬과 퀵정렬보다 우수한 정렬 알고리즘이다.
>
> 하지만, 단순 속도만 놓고 비교하면 일반적인 배열에서는 퀵정렬이 평균적으로 빠른 속도를 보여주기 때문에 실제로 힙정렬을 많이 사용하지는 않는다.