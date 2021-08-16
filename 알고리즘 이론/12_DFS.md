# 12강 깊이 우선 탐색

## DFS (Depth First Search)

## 깊은 것을 우선적으로 탐색하는 알고리즘

---

1. Stack을 활용한다. 
   - 기본적으로 재귀함수의 구조가 컴퓨터 내부의 스택 프레임에 차곡차곡 쌓이는 형태이기 때문에 stack 구조를 사용하지 않고 재귀함수형태로 구현하기도 한다.
2. 첫 번째 노드의 방문 체크를 한뒤 연결된 가지를 재귀함수 형태로 하나씩 방문
3. 재귀함수 호출시 방문체크로 탈출 조건을 만들어준다.
4. 2-3 반복 

---

**Python**

```python
# DFS (깊이 우선 탐색) 예제

import sys

link = [[], [2, 3], [1, 3, 4, 5], [1, 2, 6, 7], [2, 5], [2, 4], [3, 7], [3, 6]]
visit = [0] * len(link)

def dfs(start):
    if visit[start]:
        return
    visit[start] = 1
    sys.stdout.writelines(str(start) + '\n')
    for branch in link[start]:
        dfs(branch)

dfs(1)
```



**C++**

```C++
#include <iostream>
#include <vector>

using namespace std;

int number = 7;
int c[7];
vector<int> a[8];

void dfs(int x) {
  if(c[x]) return;
  c[x] = true;
  cout << x << ' ';
  for(int i = 0; i < a[x].size(); i++) {
    int y = a[x][i];
    dfs(y);
  }
}

int main(void) {
  a[1].push_back(2);
  a[1].push_back(1);
  
  a[1].push_back(3);
  a[3].push_back(1);
  
  a[2].push_back(3);
  a[3].push_back(2);
  
  a[2].push_back(4);
  a[4].push_back(2);
  
  a[2].push_back(5);
  a[5].push_back(2);
  
  a[4].push_back(5);
  a[5].push_back(4);
  
  a[3].push_back(6);
  a[6].push_back(3);
  
  a[3].push_back(7);
  a[7].push_back(3);
  
  a[6].push_back(7);
  a[7].push_back(6);
  
  bfs(1);
  
  return 0;
}
```



## 특징

> DFS 또한 DFS 자체로는 큰 의미가 없고 DFS를 활용해서 문제를 해결하고자 하는 것에 주안점이 두어져 있으므로 작동 원리에 대해서만 빠삭하게 이해하면 된다.

