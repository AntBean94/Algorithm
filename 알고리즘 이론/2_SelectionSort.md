# 2강 정렬 알고리즘의 개요와 선택 정렬

## Selection Sort

### "가장 작은 것을 선택해서 제일 앞으로 보낸다."

1. 앞에서 부터 뒤로 탐색한다.
2. 제일 작은 값의 위치를 저장해두고 가장 앞에있는 원소와 위치를 바꾼다.
3. 반복한다.

**Python**

```python
arr = [1, 4, 3, 6, 7, 5, 2, 9, 8]

for i in range(len(arr)):
    num = i
    for j in range(i, len(arr)):
        if arr[j] < arr[num]:
            num = j
    arr[i], arr[num] = arr[num], arr[i]
    
print(arr)
```



**C++**

```c++
int main(void) {
  int i, j, min, index, temp;
  int arr[10] = {1, 10, 5, 4, 8, 7, 6, 3, 2, 9};
  for(i = 0; i < 10; i++) {
    min = 9999;
    for(j = i; j < 10; j++) {
      if(min > array[j]) {
        min = array[j];
        index = j;
      }
    }
    temp = array[i];
    array[i] = array[index];
    array[index] = temp;
  }
  for(i = 0; i < 10; i++) {
    printf("%d ", array[i]);
  }
  return 0;
}
```



## 효율성

1. 시간 복잡도 ... O(N^2)

```markdown
길이 10인 배열

10 + 9 + 8 + ... + 2 + 1

=> 10 * (10 + 1) / 2 = 55

=> N * (N + 1) / 2

=> O(N^2)
```



=> 비효율적이다.











