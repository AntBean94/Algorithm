# 6강 병합정렬

## Merge Sort

## 일단 반으로 나누고 나중에 합쳐서 정렬하면 어떨까?

---

1. 길이가 1 또는 2인 배열이 남을 때까지 분할한다.
2. 1또는 2인 배열이 남으면 대소 관계 비교를 통해 병합한다.
3. 병합과정을 반복한다.(재귀)

**주의**

병합 정렬을 구현할 때 신경써야 하는 부분은 반드시 정렬에 사용되는 배열은 '전역 변수'로 선언해야 한다는 것이다. 함수 안에서 배열을 선언하게 된다면 매번 배열을 선언해야 한다는 점에서 메모리 자원의 낭비가 매우 커질 수 있다.

=> 기본적으로 **병합 정렬**은 '기존의 데이터를 담을 추가적인 배열 공간이 필요하다'는 점에서 메모리 활용이 비효율적이라는 문제가 있다.

---

**Python**

```python
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
```



**C++**

```C++
# include <stdio.h>

int number = 8;
int sorted[8]; // 정렬 배열은 반드시 전역 변수로 만들어 줘야 한다.

void merge(int a[], int m, int middle, int n) {
  int i = m;
  int j = middle + 1;
  int k = m;
  // 작은 순서대로 배열에 삽입
  while(i <= middle && j <= n) {
    if(a[i] <= a[j]) {
      sorted[k] = a[i];
      i++;
    } else {
      sorted[k] = a[j];
      j++;
    }
    k++;
  }
  // 남은 데이터도 삽입
  if(i > middle) {
    for(int t = j; t <= n; t++) {
      sorted[k] = a[t];
      k++;
    } 
  } else {
    for(int t = i; t <= middle; t++) {
      sorted[k] = a[t];
      k++;
    }
  }
  // 정렬된 배열을 삽입
  for(int t = m; t <= n; t++) {
    a[t] = sorted[t];
  }
}

void mergeSort(int a[], int m, int n) {
  // 크기가 1보다 큰 경우
  if(m < n) {
    int middle = (m + n) / 2;
    mergeSort(a, m, middle);
    mergeSort(a, middle + 1, n);
    merge(a, m, middle, n);
  }
}

int main(void) {
  int array[number] = {7, 6, 5, 8, 3, 5, 9, 1};
  mergeSort(array, 0, number - 1);
  for(int i = 0; i < number; i++) {
    printf("%d ", array[i]);
  }
}
```



## 효율성

### 1. 시간 복잡도 ---- N log N

분할정복의 특징이면서 데이터의 편향에 영향을 받지 않으므로 N * logN 의 효율성을 가진다.

```
1 2 3 4 5 6 7 8

1 2 3 4 | 5 6 7 8 

1 2 | 3 4 | 5 6 | 7 8

1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 ===> 시작

12 | 34 | 56 | 78

1234 | 5678

12345678

====> 가로 너비 N
			세로 높이 logN (log8 = 3 => 3층)
			
====> 너비가 N인 이유: 이미 병합하는 배열이 정렬되어있기 때문에 각각 한번씩만 조회하므로..

```