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
# 20강 위상 정렬 (Topology Sort) 예제

from collections import deque

'''
입력 예제

노드의 갯수, 간선의 갯수
간선정보

7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

'''

# 노드, 간선 갯수 정보 입력
v, e = map(int, input().split())
# 진입 차수 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담을 연결리스트 초기화
graph = [[] for _ in range(v + 1)]

# 간선 정보 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 위상정렬 함수
def topology_sort():
    result = []
    Q = deque()
    
    # 진입차수 0인 값을 찾아 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            Q.append(i)
    
    # 반복
    while Q:
        now = Q.popleft()
        result.append(now)
        for next in graph[now]:
            # 진입차수를 감소 => 간선 제거
            indegree[next] -= 1
            # 진입차수가 0이라면 Q에 삽입
            if indegree[next] == 0:
                Q.append(next)
            
    print(*result)

topology_sort()
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

