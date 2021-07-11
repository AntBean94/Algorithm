# 3강 버블 정렬

## Bubble Sort

## "옆에 있는 값과 비교해서 더 작은 값을 앞으로 보내면 어떨까?"

---

1. 가장 앞에있는 원소부터 바로 오른쪽 원소와 비교해나간다.
2. 두 원소 중, 더 큰 원소를 오른쪽으로 옮긴다.
3. 배열의 끝에 다다르면 오른쪽 끝에 가장 큰 원소가 자리한다.
4. 정렬된 원소(가장 오른쪽)를 제외하고 나머지 범위에서 반복한다.
5. 위의 과정을 다시 반복한다.

---

**Python**

```python
import sys

arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(len(arr)-1):
    for j in range(0, len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

sys.stdout.write(" ".join(map(str, arr)))
```

**C++**

```C++
int main(void) {
  int i, j, temp;
  int array[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9}
  for(i = 0; i < 10; i++) {
    for(j = 0; j < 9 - i; j++) {
      if(array[j] > array[j + 1]) {
        temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
      }
    }
  }
  for(i = 0; i < 10; i++) {
    printf("%d ", array[i]);
  }
	return 0;
}
```



## 효율성

1. 시간 복잡도 ... **O(N * N)**

   ```markdown
   10 + 9 + 8 + ... + 2 + 1
   
   => N * (N + 1) / 2
   
   => O(N * N)
   ```



그러나, 실제로 코드를 작동시켜보면 선택정렬보다 오래걸린다...

그 이유는 선택 정렬 대비 배열의 교환이 자주 일어나고 이러한 명령을 수행하는데 시간이 소모되기 때문이다.

일반적으로 정렬 중에서 **가장 느리다**

