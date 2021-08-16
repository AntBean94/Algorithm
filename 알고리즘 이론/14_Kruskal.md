# 14강 크루스칼 알고리즘

## Kruskal Algorithm

## 간선을 거리가 짧은 순서대로 그래프에 포함시키면 어떨까?

---

1. UnionFind 함수를 구현한다.

   - getParent()
   - unionParent()
   - findParent()

2. Kruskal 알고리즘 구현

   - 간선 정보, 부모 정보, 노드 갯수를 인자로 받는다.

     kruskal(graph, parent, node)

   - 간선 정보를 간선비용 기준으로 정렬한다.

     graph.sort(key=lambda x: x[])

   - 간선 정보를 앞에서부터 하나씩 탐색하며 다음의 과정을 수행
     - 두 노드로 findParent() 함수 실행
     - True) 다음 간선정보로 건너뛰기
     - False) 두 노드로 unionParent() 함수 실행하고 다음 간선정보 확인
   - (간선 = 노드 갯수 - 1) 을 만족하면 종료 (필수조건은 아님/시간 감소를 위해..)

---

**Python**

```python
# 크루스칼 알고리즘 (Kruskal Algorithm) 예제

# unionfind 구현
def getParent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = getParent(parent, parent[x])
    return parent[x]

def unionParent(parent, x, y):
    a = getParent(parent, x)
    b = getParent(parent, y)
    if a < b: parent[b] = a
    else: parent[a] = b

def findParent(parent, x, y):
    a = getParent(parent, x)
    b = getParent(parent, y)
    if a == b: return True
    else: return False

# kruskal 알고리즘 구현
def kruskal(graph, min_tree, node):
    graph.sort(key=lambda x: x[2])

    value = 0
    line_num = node - 1
    key = 0
    while line_num > 0:
        a = graph[key][0]
        b = graph[key][1]
        if findParent(min_tree, a, b):
            key += 1
        else:
            unionParent(min_tree, a, b)
            value += graph[key][2]
            line_num -= 1
            key += 1
    return value

# 노드의 갯수
node = 7
# 최소신장 트리
min_tree = [i for i in range(node+1)]
# 간선 정보
graph = [[1, 7, 12],
        [1, 4, 28],
        [1, 2, 67],
        [1, 5, 17],
        [2, 4, 24],
        [2, 5, 62],
        [3, 5, 20],
        [3, 6, 37],
        [4, 7, 13],
        [5, 6, 45],
        [5, 7, 73]]

print(kruskal(graph, min_tree, node))
print(min_tree)
```



**C++**

```C++
#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorighm>

using namespace std;

// 부모 노드를 찾는 함수
int getParent(int parent[], int x) {
  if(parent[x] == x) return x;
  return parent[x] = getParent(parent, parent[x]);
}

// 두 부모 노드를 합치는 함수
int unionParent(int parent[], int a, int b) {
  a = getParent(parent, a);
  b = getParent(parent, b);
  if(a < b) parent[b] = a;
  else parent[a] = b;
}

// 같은 부모를 가지는지 확인
int findParent(int parent[], int a, int b) {
  a = getParent(parent, a);
  b = getParent(parent, b);
  if(a == b) return 1;
  else return 0;
}

// 간선 클래스 선언
class Edge {
public:
  int node[2];
  int distance;
  Edge(int a, int b, int distance) {
    this->node[0] = a;
    this->node[1] = b;
    this->distance = distance;
  }
  bool operator <(Edge &edge) {
    return this->distance < edge.distance;
  }
}

int main(void) {
  int n = 7;
  int m = 11;
  
  vector<Edge> v;
  v.push_back(Edge(1, 7, 12));
  v.push_back(Edge(1, 4, 28));
  v.push_back(Edge(1, 2, 67));
  v.push_back(Edge(1, 5, 17));
  v.push_back(Edge(2, 4, 24));
  v.push_back(Edge(2, 5, 62));
  v.push_back(Edge(3, 5, 20));
  v.push_back(Edge(3, 6, 37));
  v.push_back(Edge(4, 7, 13));
  v.push_back(Edge(5, 6, 45));
  v.push_back(Edge(5, 7, 73));
  
  // 간선의 비용을 기준으로 오름차순 정렬
  sort(v.begin(), v.end());
  
  // 각 정점이 포함된 그래프가 어디인지 저장
  int parent[n];
  for(int i = 0; i < n; i++) {
    parent[i] = i;
  }
  
  int sum = 0;
  for(int i = 0; i < v.size(); i++) {
    // 사이클이 발생하지 않는 경우 그래프에 포함
    if(!findParent(parent, v[i].node[0] - 1, v[i].node[1] - 1)) {
      sum += v[i].distance;
      unionParent(parent, v[i].node[0] - 1, v[i].node[1] - 1);
    }
  }
  printf("%d\n", sum);
}
```

