# 20강 위상 정렬

## Topology Sort

## 순서가 정해져있는 작업을 수행해야 할 때, 그 순서를 결정해보자

---

**진입차수**: 노드를 향해 들어오는 간선의 갯수

**사용 조건**: 사이클이 존재하지 않는 방향 그래프에만 사용 가능

1. 진입차수가 0인 정점을 큐에 삽입한다.
2. 큐에서 원소를 꺼내 연결된 모든 간선을 제거한다.
3. 간선 제거 이후에 진입차수가 0이 된 정점을 큐에 삽입한다.
4. 큐가 빌 때까지 2 ~ 3번 과정을 반복한다.
   - 이 때, 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재하는 것
   - 모든 원소를 방문했다면 큐에서 꺼낸 순서가 위상 정렬의 결과

---

**Python**

```python
```



**C++**

```C++
#include <iostream>
#include <vector>
#include <queue>
#define MAX 10

using namespace std;

int n, inDegree[MAX];
vector<int> a[MAX];

void topologySort() {
  int result[MAX];
  queue<int> q;
  // 진입차수가 0인 노드를 큐에 삽입한다.
  for(int i = 1; i <= n; i++) {
    if(inDegree[i] == 0) q.push(i);
  }
  // 위상 정렬이 완전히 수행되려면 정확히 N개의 노드를 방문
  for(int i = 1; i <= n; i++) {
    if(q.empty()) {
      printf("사이클이 발생했습니다.");
      return;
    }
    int x = q.front();
    q.pop();
    result[i] = x;
    for(int i = 0; i < a[x].size(); i++) {
      int y = a[x][i];
      if(--inDegree[y] == 0) {
        q.push(y);
      }
    }
  }
  for(int i = 1; i <= n; i++) {
    printf("%d ", result[i]);
  }
}

int main(void) {
  n = 7;
  a[1].push_back(2);
  inDegree[2]++;
  a[1].push_back(5);
  inDegree[5]++;
  :
  :
  :
  :
  topologySort();
}

```

