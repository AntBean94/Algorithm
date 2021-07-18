# 8강 계수 정렬

## Counting Sort

## 크기를 기준으로 갯수를 센다.

---

**범위가 한정된 배열 기준 O(N)의 시간복잡도**를 가지므로 굉장히 빠른 정렬알고리즘이다.

1. 배열의 첫 번째 원소부터 탐색을 시작
2. 계수 배열의 각 원소에 맞는 숫자를 인덱스로 1씩 증가
3. 배열의 끝까지 탐색
4. 계수배열의 인덱스를 배열의 원소 크기만큼 반복출력

---

**Python**

```python 
# 계수 정렬 (Counting Sort) 예제

import sys 

arr = [1, 3, 2, 4, 1, 3, 2, 2, 5, 4, 2, 3, 4, 1, 5, 5, 1]
rng = 5     # 범위

def CountingSort(arr, n):
    cnt_arr = [0] * n
    for a in arr:
        cnt_arr[a - 1] += 1
    print(cnt_arr)
    for i in range(n):
        num = i + 1
        for _ in range(cnt_arr[i]):
            sys.stdout.write("%d " %num)

CountingSort(arr, rng)
```



**C++**

```C++
#include <stdio.h>

int main(void) {
  int temp;
  int count[5];
  int array[30] = {
    1, 3, 2, 4, 3, 2, 5, 4, 3, 2, 
    4, 1, 2, 3, 1, 4, 5, 5, 2, 4,
    1, 5, 2, 5, 3, 2, 4, 3, 3, 1
  };
  for(int i = 0; i < 5; i++) {
    count[i] = 0;
  }
  for(int i = 0; i < 30; i++) {
    temp = array[i];
    count[temp - 1]++;
  }
  for(int i = 0; i < 5; i++) {
    if(count[i] != 0) {
      for(int j = 0; j < count[i]; j++) {
        printf("%d ", i + 1);
      }
    }
  }
}
```



## 효율성

1. 시간복잡도 ... 0(N)

   - 범위가 한정되어 있는 경우 굉장히 빠른 시간복잡도를 보여준다.
   - 하지만 데이터의 범위에 많은 영향을 받기 때문에 항상 사용할 수 있는 알고리즘은 아니다.
   - 특정 조건(데이터의 범위가 좁거나 알려져있는 경우)에서 굉장히 빠른 알고리즘이다.
   - 배열의 수를 한번씩만 탐색하면 되기 때문에 시간복잡도는 O(N)

   