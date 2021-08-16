# 9강 스택

## Stack

## 후입선출 (LIFO: Last In First Out)

---

1. Python에서는 stack 자료형을 따로 제공하지 않는다.
2. list를 사용해 stack을 흉내낼 수 있다.
3. append() 메서드를 사용해 push를 한다.
4. pop() 메서드를 사용해 마지막 원소를 pull한다.

---

**Python**

```python
# 1, 2, 3 을 순차적으로 넣고 빼보자

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
for i in range(len(stack)):
  print(stack.pop())

```



**C++**

```c++
#include <iostream>
#include <stack>

using namespace std;

int main(void) {
  stack<int> s;
  s.push(7);
  s.push(5);
  s.push(4);
  s.pop();
  s.push(6);
  s.pop();
  while(!s.empty()) {
    cout << s.top() << ' ';
    s.pop();
  }
  return 0;
}
```



