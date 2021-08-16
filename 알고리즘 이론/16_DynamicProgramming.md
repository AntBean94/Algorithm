# 16강 다이나믹 프로그래밍

## Dynamic Programming

## 하나의 문제는 단 한 번만 풀도록 하는 알고리즘

---

**가정**

1. 큰 문제를 작은 문제로 나눌 수 있어야 한다.
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

**특징**

1. 메모이제이션 (Memoization) 사용
2. 분할정복의 비효율성을 개선

---

**Python**

```python
# 16강 다이나믹 프로그래밍 (Dynamic Programming) 예제

# fibonacci 수열 (상향식)
def Fibo_dp_up(n):
    arr = [0] * n
    for i in range(0, n):
        if i < 2:
            arr[i] = 1
        else:
            arr[i] = arr[i-1] + arr[i-2]
    return arr[n-1]

# 재귀
def Fibo_recur(n):
    if n == 1: return 1
    if n == 2: return 1
    return Fibo_recur(n-1) + Fibo_recur(n-2)

# 재귀 => dp (memoization)
arr = [0] * 100
def Fibo_dp(n):
    if n == 1: return 1
    if n == 2: return 1
    if arr[n] != 0:
        return arr[n]
    return Fibo_dp(n - 1) + Fibo_dp(n - 2)    


print(Fibo_dp_up(int(input())))    
```



**C++**

```C++
#include <stdio.h>

// 재귀
int dp(int x) {
  if(x == 1) return 1;
  if(x == 2) return 1;
  return dp(x - 1) + dp(x - 2);
}

// dp
int d[100];

int dp(int x) {
  if(x == 1) return 1;
  if(x == 2) return 1;
  if(d[x] != 0) return d[x];
  return d[x] = dp(x - 1) + dp(x - 2);
}

int main(void) {
  printf("%d", dp(10))
}
```



## 효율성

피보나치 수열을 재귀로 풀게 되면 시간복잡도는 2^N 회의 계산을 해야한다.

즉 50번째 항을 구하기 위해서는 1,000,000,000,000,000 번의 계산을 해야한다는것!

하지만 dp를 사용하게 되면 각각의 항은 한번씩만 계산되므로 n의 시간복잡도를 가지게 된다.