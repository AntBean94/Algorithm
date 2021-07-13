# 5강 퀵 정렬

## Quick Sort

## "특정한 값을 기준으로 큰 숫자와 작은 숫자를 나누면 어떨까?"

> 퀵 정렬은 하나의 큰 문제를 두개의 작은 문제로 분할하는 방식으로 빠르게 문제를 해결한다.
>
> 퀵 정렬이 빠른 이유는 피봇(pivot) 값을 기준으로 큰 값과 작은 값이 각각 정렬할 때 서로의
>
> 영역을 침범하지 않기 때문이다. 
>
> 경우의 수를 계산해봐도 10개의 수를 정렬하기 위해 모든 수를 2개의 반복문으로 정렬하게
>
> 되면 10 * 10 = 100 의 경우의 수가 나오지만 각각 분할해서 정복하면
>
> (5 * 5 = 25) + (5 * 5 = 25) = 50 으로 경우의 수가 확연히 감소함을 알 수 있다.

---

1. 배열의 첫 번째 값을 **피봇** 값으로 설정한다.
2. 배열의 왼쪽부터 피봇값보다 큰 첫 번째 값을 찾는다.
3. 배열의 오른쪽부터 피봇값보다 작은 첫 번째 값을 찾는다.
4. 이 찾은 두개의 값을 비교해 `큰 값의 인덱스`가 `작은 값의 인덱스`보다 **작다면** 두 수를 교환한다.
5. 위의 과정을 반복하다가 `큰 값의 인덱스` 가 `작은 값의 인덱스` 보다 **큰** 경우를 **'엇갈리다'** 라고 표현한다.
6. 엇갈린경우 찾은 작은 값과 피봇값을 서로 교환한다.
7. 피봇값을 기준으로 배열을 둘로 나누고 위의 과정을 각각 반복한다.

---

**Python**

```python
# 퀵 정렬(Quick Sort) 예제

import sys

arr = [120, 19, 18, 17, 16, 10,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

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
```



**C++**

```C++
int number = 10;
int data[10] = {1, 10, 9, 8, 7, 6, 5, 4, 3, 2}

void QuickSort(int *data, int start, int end) {
  if (start  >= end) { // 원소가 1개인 경우
    return;
  }
  
  int key = start; // key는 첫 번째 원소
  int i = start + 1;
  int j = end;
  int temp;
  while (i <= j) { // 엇갈릴 때까지 반복
    while (data[i] <= data[key]) { // 키 값보다 큰 값을 만날 때까지
      i++;
    }
    while (data[j] >= data[key] && j > start) { // 키 값보다 작은 값을 ...
      j--;
    }
    if (i > j) { // 엇갈린 상태라면 키값과 교환
      temp = arr[j];
      arr[j] = arr[key];
      arr[key] = temp;
    } else {
      temp = arr[i];
      arr[i] = arr[j];
      arr[j] = temp;
    }
  }
  QuickSort(data, start, j - 1);
  QuickSort(data, j + 1, end);
}

int main(void) {
  QuickSort(data, 0, number - 1);
  for(int i = 0; i < number; i++) {
    printf("%d ", data[i])
  }
}
```



## 효율성

> 일반적으로 N logN 의 시간복잡도를 가지고 있으며 평균적으로 가장 빠른 정렬 알고리즘이다. 하지만 치명적인 약점이 있는데 **이미 정렬이 충분히 된 배열**의 경우 제일 비효율적인 정렬속도를 보여준다. 예를 들어 [1, 2, 3, 4] 배열의 경우 왼쪽부터 오른쪽, 오른쪽부터 왼쪽까지 탐색을 하고도 1 하나만 정렬이 된다. 따라서 N * N 의 시간복잡도를 가지게 된다. 이는 퀵 정렬의 장점인 **분할 정복**을 사용하지 못함을 의미한다.
>
> 데이터가 충분히 정렬된 상태라면 삽입 정렬과 같은 정렬방법이, 그렇지 않다면 퀵 정렬이 좋은 효율성을 보여줄 수 있다. 어떤 정렬 알고리즘이 더빠르다는 논쟁은 의미가 없다.
>
> 따라서, 상황에 맞는, 데이터의 특성에 맞는 정렬알고리즘을 선택하는 것이 중요하다.

