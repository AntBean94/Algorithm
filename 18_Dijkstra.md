# 18강 다익스트라 알고리즘

## Dijkstra Algorithm

## 최단 거리는 여러 개의 최단 거리로 이루어져 있다!

---

"다익스트라 알고리즘으로 특정한 하나의 정점에서 다른 모든 정점으로 가는 최단 경로를 알 수 있다."

1. 출발 노드를 설정한다.
2. 출발 노드를 기준으로 각 노드의 최소 비용을 저장한다.
3. 방문하지 않은 노드 중에서 가장 비용이 적은 노드를 선택한다.
4. 해당 노드를 거쳐서 특정한 노드로 가는 경우를 고려하여 최소 비용을 갱신한다.
5. 위 과정에서 3번 ~ 4번을 반복한다.

---

**Python**

#### 1. 선형 탐색 알고리즘 O(N^2)

```python
# 18강 다익스트라 알고리즘 (Dijkstra Algorithm) 예제 (1)
# 선형 탐색 알고리즘 - O(N^2)

n = 6
INF = 1000000000
a = [[0, 2, 5, 1, INF, INF],
    [2, 0, 3, 2, INF, INF],
    [5, 3, 0, 3, 1, 5],
    [1, 2, 3, 0, 1, INF],
    [INF, INF, 1, 1, 0, 2],
    [INF, INF, 5, INF, 2, 0]]

v = [0] * n
d = [0] * n

# 최단거리 반환 함수
def getSmallIndex():
    m = INF
    index = 0
    for i in range(n):
        if d[i] < m and not v[i]:
            m = d[i]
            index = i
    return index

# 다익스트라 알고리즘 수행 함수
def dijkstra(start):
    # 거리 초기화
    for i in range(n):
        d[i] = a[start][i]
    v[start] = 1
    # 최단거리 찾아가며 거리 수정
    for i in range(n - 1):
        cur = getSmallIndex()
        v[cur] = 1
        for j in range(n):
            if not v[j] and d[cur] + a[cur][j] < d[j]:
                d[j] = d[cur] + a[cur][j]

dijkstra(0)
print(*d)
```



#### 2. Heap 활용: O(NlogN)

```python
```





**C++**

#### 1. 선형 탐색 알고리즘: O(N^2)

```C++
#include <stdio.h>

int number = 6;
int INF = 1000000000;

// 전체 그래프를 초기화한다.
int a[6][6] = {
  {0, 2, 5, 1, INF, INF},
  {2, 0, 3, 2, INF, INF},
  {5, 3, 0, 3, 1, 5},
  {1, 2, 3, 0, 1, INF},
  {INF, INF, 1, 1, 0, 2},
  {INF, INF, 5, INF, 2, 0},
};
bool v[6]; // 방문 체크
int d[6]; // 최단 거리 체크

// 가장 최소 거리를 가지는 정점을 반환한다.
int getSmallIndex() {
  int min = INF;
  int index = 0;
  for(int i = 0; i < number; i++) {
    if(d[i] < min && !v[i]) {
      min = d[i];
      index = i;
    }
  }
  return index;
}

// 다익스트라를 수행하는 함수
void dijkstra(int start) {
  for(int i = 0; i < number; i++) {
    d[i] = a[start][i];
  }
  v[start] = true;
  for(int i = 0; i < number - 1; i++) {
    int current = getSmallIndex();
    v[current] = true;
    for(int j = 0; j < 6; j++) {
      if(!v[j]) {
        if(d[current] + a[current][j] < d[j]) {
          d[j] = d[current] + a[current][j];
        }
      }
    }
  }
}

int main(void) {
  dijkstra(0);
  for(int i = 0; i < number; i++) {
    printf("%d ", d[i]); // 0 2 3 1 2 4
  }
}
```



#### 2. Heap 활용: O(NlogN)

```C++
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int number = 6;
int INF = 1000000000;

vector<pair<int, int> > a[7]; // 간선 정보
int d[7];	// 최소 비용

void dijkstra(int start) {
  d[start] = 0;
  priority_queue<pair<int, int> > pq; // 힙 구조입니다.
  // 가까운 순서대로 처리하므로 큐를 사용한다.
  while(!pq.empty()) {
    int current = pq.top().first;
    // 짧은 것이 먼저 오도록 음수화(-) 한다.
    int distance = -pq.top().second;
    pq.pop();
    // 최단 거리가 아닌 경우 스킵한다.
    if(d[current] < distance) continue;
    for(int i = 0; i < a[current].size(); i++) {
      // 선택된 노드의 인접 노드
      int next = a[current][i].first;
      // 선택된 노드 거쳐서 인접 노드로 가는 비용
      int nextDistance = distance + a[current][i].second;
      // 기존의 최소 비용보다 더 저렴하다면 교체한다.
      if(nextDistance < d[next]) {
        pq.push(make_pair(next, -nextDistance))
      }
    }
  }
}

int main(void) {
  // 기본적으로 연결되지 않은 경우 비용은 무한이다.
  for(int i = 1; i <= number; i++) {
    d[i] = INF;
  }
  
  a[1].push_back(make_pair(2, 2));
  a[1].push_back(make_pair(3, 5));
  a[1].push_back(make_pair(4, 1));
  
  a[2].push_back(make_pair(1, 2));
  a[2].push_back(make_pair(3, 3));
  a[2].push_back(make_pair(4, 2));
  
  a[3].push_back(make_pair(1, 5));
  a[3].push_back(make_pair(2, 3));
  a[3].push_back(make_pair(4, 3));
  a[3].push_back(make_pair(5, 1));
  a[3].push_back(make_pair(6, 5));
  
  a[4].push_back(make_pair(1, 5));
  a[4].push_back(make_pair(1, 5));
  a[4].push_back(make_pair(1, 5));
  a[4].push_back(make_pair(1, 5));

  a[5].push_back(make_pair(3, 1));
  a[5].push_back(make_pair(4, 1));
  a[5].push_back(make_pair(6, 2));

  a[6].push_back(make_pair(3, 5));
  a[6].push_back(make_pair(5, 2));
	
  dijkstra(1);
  
  // 결과 출력
  for(int i = 1; i <= number; i++) {
    printf("%d ", d[i]);
  }
}

```

