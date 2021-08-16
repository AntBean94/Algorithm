# 22강 네트워크 플로우

## Network Flow

## 최대 유량을 계산해보자

---

#### 네트워크 플로우란?

"특정한 지점에서 다른 지점으로 데이터가 얼마나 많이 흐르고 있는가"를 측정하는 알고리즘

**유량 표현 방식**

##### 용량(Capacity)  (A) -----8----- (B) -----6----- (C) -----7----- (D)

##### 유량(Flow)        (A) ----6/8---- (B) ----6/6---- (C) ----6/7---- (D)



#### 에드몬드 카프(Edmonds-Karp) 알고리즘

BFS를 이용해서 최대유량을 계산하는 알고리즘

1. 현재 흐르고 있는 유량(Flow)를 0으로 설정
2. 이후 정해진 용량(Capacity) 안에서 가능한 용량의 양을 반복적으로 더한다.

더 이상 흐를수 있는 경우가 없을 때 **"음의 유량"** 개념을 사용한다.

남아있는 모든 가능한 경로를 더 찾아낼 수 있다. (음의 유량을 활용해서)

**최대 유량 알고리즘은 순서가 상관없다.** 

남아있는 양이 1이 넘으면 계속해서 흘려 보내주면 알아서 최적화가 이루어진다.



**Python**

```python
# 22강 네트워크 플로우 (Network Flow) 예제

'''
네트워크 플로우 예제 입력값

start(시작), end(종료)
V(노드 갯수), E(간선 갯수)
간선 정보
노드 노드 용량

1 6
6 10
1 2 12
1 4 11
2 3 6
2 4 3
2 5 5
2 6 9
3 6 8
4 5 9
5 3 3
5 6 4

'''
from collections import deque 

INF = 1000000000

start, end = map(int, input().split())
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
C = [[0] * (V+1) for _ in range(V+1)]
F = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    C[a][b] = c
result = 0

def maxFlow(start, end):
    global result
    while True:
        visit = [-1] * (V+1)
        Q = deque()
        Q.append(start)
        while Q:
            x = Q.popleft()
            for y in graph[x]:
                # 방문기록이 없고 용량이 남은경우
                if C[x][y] - F[x][y] > 0 and visit[y] == -1:
                    Q.append(y)
                    visit[y] = x
                    if y == end: break
        
        # 모든 경로를 다찾아서 더이상 도달할 수 없는경우(while 탈출)
        if visit[end] == -1: break
        # 경로의 유량
        flow = INF
        # 가능한 최소유량을 거꾸로 탐색해간다.
        pre = end
        while pre != start:
           now = visit[pre]
           flow = min(flow, C[now][pre] - F[now][pre])
           pre = now
        # 최소유량을 더한다.
        pre = end
        while pre != start:
            now = visit[pre]
            F[now][pre] += flow
            F[pre][now] -= flow
            pre = now
        result += flow
        
maxFlow(start, end)
print(result)
```



**C++**

```C++
#include <iostream>
#include <vector>
#include <queue>

#define MAX 100
#define INF 1000000000

using namespace std;

int n = 6, result;
int c[MAX][MAX], f[MAX][MAX], d[MAX];
vector<int> a[MAX];

void maxFlow(int start, int end) {
  while(1) {
    fill(d, d + MAX, -1); // 모든 정점의 방문상태 초기화
    queue<int> q;
    q.push(start);
    while(!q.empty()) {
      int x = q.front();
      q.pop();
      for(int i = 0; i < a[x].size(); i++) {
        int y = a[x][i];
        // 방문하지 않은 노드 중에서 용량이 남은 경우
        if(c[x][y] - f[x][y] > 0 && d[y] == -1) {
          q.push(y);
          // 방문체크 (경로를 기억하기 위해 부모를 넣어준다.)
          d[y] = x;
          // 도착지에 도달한 경우 break
          if(y == end) break;
        }
      }
    }
    // 모든 경로를 다 찾은 뒤에 탈출한다.(while문 탈출조건)
    if(d[end] == -1) break;
    // 경로의 유량
    int flow = INF;
    // 거꾸로 최소 유량을 탐색한다.
    for(int i = end; i != start; i = d[i]) {
      // 자식 => 부모로 가는 경로의 유량을 최솟값으로 계속 바꿔준다.
      // => min(flow, 용량 - 유량)
      flow = min(flow, c[d[i]][i] - f[d[i]][i]);
    }
    // 최소 유량만큼 추가한다.
    for(int i = end; i != start; i = d[i]) {
      f[d[i]][i] += flow;
      f[i][d[i]] -= flow;
    }
    result += flow;
  }
}

int main(void) {
  a[1].push_back(2);
  a[2].push_back(1);
  c[1][2] = 12;
  :
  :
  :
  a[5].push_back(6);
  a[6].push_back(5);
  c[5][6] = 4;
  
  maxFlow(1, 6);
  printf("%d", result);
}
```



## 정리

에드몬드 카프 알고리즘의 시간 복잡도는 **O(VE^2)**



