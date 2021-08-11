# 21강 강한 결합 요소

## Strongly Connected Component (SCC)

#### 모든 정점에 대해 DFS를 수행해 SCC를 추출해보자

---

#### 강한결합요소란?

**강한 결합 요소**란 그래프 안에서 '강하게 결합된 정점 집합'을 의미

SCC는 '같은 SCC에 속하는 두 정점은 서로 도달이 가능하다'는 특징이 있음

- 사이클이 발생하는 경우 무조건 SCC에 해당

- 무향그래프라면 그 그래프는 무조건 SCC(방향이 있을때만 의미가 있음)



#### SCC를 추출하는 대표적인 알고리즘

1. **코사라주 알고리즘(Kosaraju's Algorithm)**

   - 구현에 용이

2. **타잔 알고리즘(Tarjan's Algorithm)**

   - 모든 정점에 대해 DFS를 수행하여 SCC를 찾는 알고리즘

   - 적용에 용이

타잔알고리즘 적용이 더 쉬우므로 타잔알고리즘을 다뤄보자



#### 구현

1. 모든 정점에 대하여 DFS를 실시한다.
2. DFS를 수행하며 다음 노드가 스택에 쌓여있는지 확인한다.
3. 스택에 쌓여있다면 다음노드의 부모노드를 찾아가면 하나씩 뽑아낸다.
4. 부모노드가 자기 자신과 같다면 자기자신까지를 강한결합요소에 포함시킨다.
5. 반복



**Python**

```python
# 21강 강한 결합 요소 (Strongly Connected Component) 예제

id = 1
MAX = 10001
d = [0] * MAX
finished = [False] * MAX
stack = []
SCC = []

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for i in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

def dfs(x):
    global id
    d[x] = id
    id += 1

    stack.append(x)
    parent = d[x]
    for i in range(len(graph[x])):
        y = graph[x][i]
        # 방문하지 않았다면
        if d[y] == 0: parent = min(parent, dfs(y))
        # 진행중이라면
        elif not finished[y]: parent = min(parent, d[y])
    # 부모 노드가 자기 자신인 경우
    if parent == d[x]:
        scc = []
        while True:
            t = stack.pop()
            scc.append(t)
            finished[t] = True
            if t == x:
                break
        SCC.append(scc)
    # 부모 반환
    return parent

for i in range(1, V):
    if d[i] == 0:
        dfs(i)

# 출력
print(f"SCC의 갯수는: {len(SCC)}")
for i in range(len(SCC)):
    print(f"{i}번째 SCC: ", end="")
    for j in SCC[i]:
        print(j, end=" ")
    print()
```



**C++**

```C++
#include <iostream>
#include <vector>
#include <stack>
#define MAX 10001

using namespace std;

int id, d[MAX];
bool finished[MAX];
vector<int> a[MAX];
vector<vector<int> > SCC;
stack<int> s;

// DFS는 총 정점의 갯수만큼 실행된다.
int dfs(int x) {
  d[x] = ++id; // 노드마다 고유한 번호 할당
  s.push(x); // 스택에 자기 자신을 삽인한다.
  
  int parent = d[x];
  for(int i = 0; i < a[x].size(); i++) {
    int y = a[x][i];
    // 방문하지 않은 이웃
    if(d[y] == 0) parent = min(parent, dfs(y));
    // 처리중인 이웃
    else if(!finished[y]) parent = min(parent, d[y]);
  }
  // 부모노드가 자기 자신인 경우
  if(parent == d[x]) {
    vector<int> scc;
    while(1) {
      int t = s.top();
      s.pop();
      scc.push_back(t);
      finished[t] = true;
      if(t == x) break;
    }
    SCC.push_back(scc);
  }
  // 자신의 부모 값을 반환
  return parent;
}

int main(void) {
  int v = 11;
  a[1].push_back(2);
  a[2].push_back(3);
  a[3].push_back(1);
  :
  :
  :
  a[10].push_back(11);
  a[11].push_back(3);
  a[11].push_back(8);
  for(int i = 1; i <= v; i++) {
    if(d[i] == 0) dfs(i);
  }
  printf("SCC의 갯수: %d\n", SCC.size());
  for(int i = 0; i < SCC.size(); i++) {
    printf("%d번 째 SCC: ", i + 1);
    for(int j = 0; j < SCC[i].size(); j++) {
      printf("%d ", SCC[i][j]);
    }
    printf("\n");
  }
  return 0
}

```



## 정리

추출된 SCC는 각 SCC들을 기준으로 **위상 정렬**을 수행할 수 있다.

또한, 타잔 알고리즘의 시간 복잡도는 **O(V + E)**로 위상 정렬의 시간 복잡도와 동일하다.

