# 13강 합집합 찾기

## Union-Find

## 두 노드가 서로 같은 그래프에 속하는지 판별해보자.

---

1. 부모 노드를 찾는 함수(**getParent**)
   - 재귀 함수를 통해 간단한 구조로 구현한다.
   - 부모를 찾으면 부모값을 리턴받으며 모든 자식의 부모를 수정한다.
2. 두 부모 노드를 합치는 함수(**unionParent**)
   - 두 원소의 부모노드를 찾는다.(getParent 활용)
   - 두 원소의 부모노드 크기를 비교한 뒤 더 작은값을 부모노드로 적용한다.
3. 같은 부모를 가지는지 확인하는 함수(**findParent**)
   - 두 원소의 부모노드를 찾는다.(getParent 활용)
   - 부모가 같으면 True 반환
   - 다르면 False 반환

---

**Python**

```python
# 합집합 찾기 (Union-Find) 예제

parent = [i for i in range(11)]

# 부모 노드를 찾는 함수
def getParent(parent, x):
    if parent[x] == x: return x
    parent[x] = getParent(parent, parent[x])
    return parent[x]

# 두 부모 노드를 합치는 함수
def unionParent(parent, x, y):
    a = getParent(parent, x)
    b = getParent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 같은 부모를 가지는지 확인
def findParent(parent, x, y):
    a = getParent(parent, x)
    b = getParent(parent, y)
    if a==b:
        return True
    else:
        return False
    
unionParent(parent, 1, 2)
unionParent(parent, 2, 3)
unionParent(parent, 3, 4)
unionParent(parent, 5, 6)
unionParent(parent, 6, 7)
unionParent(parent, 7, 8)
print(f"1과 5는 연결되어있나요? {findParent(parent, 1, 5)}")
unionParent(parent, 1, 5)
print(f"1과 5는 연결되어있나요? {findParent(parent, 1, 5)}")

```



**C++**

```C++
#include <stdio.h>

// 부모 노드를 찾는 함수
int getParent(int parent[], int x) {
  if (parent[x]==x) return x;
  return parent[x] = getParent(parent, parent[x]);
}

// 두 부모 노드를 합치는 함수
int unionParent(int parent[], int x, int y) {
  int a = getParent(parent, x);
  int b = getParent(parent, y);
  if (a < b) parent[b] = a;
  else parent[a] = b;
}

// 같은 부모를 가지는지 확인
int findParent(int parent[], int x, int y) {
  int a = getParent(parent, x);
  int b = getParent(parent, y);
  if (a==b) return 1;
  else return 0;
}

int main(void) {
  int parent[11];
  for(int i = 1; i <= 10; i++) {
    parent[i] = i;
  }
  
  unionParent(parent, 1, 2);
  unionParent(parent, 2, 3);
  unionParent(parent, 3, 4);
  unionParent(parent, 5, 6);
  unionParent(parent, 6, 7);
  unionParent(parent, 7, 8);
  printf("1과 5는 연결되어 있나요? %d\n", findParent(parent, 1, 5)); // 0
  unionParent(parent, 1, 5);
  printf("1과 5는 연결되어 있나요? %d\n", findParent(parent, 1, 5)); // 1
}
```



## 특징

> 개념적으로 굉장히 이해하기 쉽고 직관적이다.
>
> 크루스칼 알고리즘 등 고급 알고리즘에 활용되므로 잘 익혀두자.