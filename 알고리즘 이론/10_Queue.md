# 10강 큐

## Queue

## 선입선출 (FIFO: First In First Out)

---

1. 양쪽이 뚫려있는 터널 구조
2. 먼저 입장한 태스크가 먼저 처리되는 구조

### 사용방법 (Python)

##### 1. 리스트 활용

 list 객체의 pop(0) 함수를 사용하는 방법

```python
# 1. 선언
queue = list()

# 2. 데이터 삽입
queue.append()

# 3. 데이터 출력
queue.pop(0)
```

- 장점: list 자료형을 사용하기 때문에 **데이터 무작위 접근에 유리** | 시간복잡도 O(1)

- 단점: 앞에서 데이터를 출력시 리스트 전체 원소가 앞으로 한 칸씩 이동해야하기 때문에 **데이터가 많아질수록 비효율적임** | 시간복잡도 O(N)

##### 2. deque 활용

collections 모듈의 deque를 사용하는 방법

```python
# 0. 호출
from collections import deque

# 1. 선언
queue = deque([1, 2, 3])

# 2. 데이터 삽입
queue.append()

# 3. 데이터 출력(왼쪽 흐름)
queue.popleft()
```

- 장점: popleft() 메서드의 **시간복잡도가 O(1)** 이므로 **데이터 입,출력에 매우 유리**
- 단점: 링크드 리스트를 사용하기 때문에 **무작위 접근에 불리** | 시간복잡도 O(N)
- 우선순위큐 사용법: https://docs.python.org/3.8/library/collections.html#collections.deque

##### 3. Queue 클래스 활용

queue 모듈의 Queue 클래스를 활용하는 방법

```python
# 0. 호출
from queue import Queue

# 1. 선언
queue = Queue([1, 2, 3])

# 2. 데이터 삽입
queue.put()

# 3. 데이터 출력
queue.get()
```

장점 및 단점: deque와 유사

자세한 정보: https://docs.python.org/3/library/queue.html

---

### 사용방법 (C++)

##### 1. STL queue 라이브러리 활용

```C++
#include <iostream>
#include <queue>

using namespace std;

int main(void) {
  queue<int> q;
  q.push(7);
  q.push(5);
  q.push(4);
  q.pop();
  q.push(6);
  q.pop();
  while(!q.empty()) {
    cout << q.front() << ' ';
    q.pop();
  }
  return 0;
}
```

