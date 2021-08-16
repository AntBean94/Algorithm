# 17 에라토스테네스의 체

## Sieve of Eratosthenes

## 소수를 대량으로 빠르고 정확하게 구하기

---

1. 배열을 각각의 인덱스에 맞게 초기화
2. 1부터 수의 끝까지 자기 자신을 제외한 수의 배수를 제거
3. 배열의 0이 아닌 수 출력

---

**Python**

```python
# 17강 에라토스테네스의 체 (Sieve of Eratosthenes) 예제

import sys

n = int(input())
arr = [i for i in range(n+1)]
for i in range(2, n+1):
    k = 2
    if arr[i] == 0:
        continue
    else:
        while i * k <= n:
            arr[i*k] = 0
            k += 1
def f(x):
    return x > 0
sys.stdout.write(" ".join(map(str, filter(f, arr))))
```



**C++**

```C++
#include <stdio.h>

int number = 100000;
int a[100001];

void primeNumberSieve() {
  for(int i = 2; i <= number; i++) {
    a[i] = i
  }
  for(int i = 2; i <= number; i++) {
    if(a[i] == 0) continue;
    for(int j = i + i; j <= number; j += i) {
      a[j] = 0;
    }
  }
  for(int i = 2; i <= number; i++) {
    if(a[i] != 0) printf("%d ", a[i]);
  }
}

int main(void) {
  primeNumberSieve();
}
```

