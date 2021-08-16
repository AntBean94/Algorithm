# 11강 너비 우선 탐색

## BFS (Breadth First Search)

## 너비를 우선으로 탐색을 수행하는 탐색 알고리즘

---

1. Queue를 활용한다.
2. 첫 번째 노드를 queue에 넣고 방문처리한다.
3. queue의 첫 번째 원소를 pop한뒤 인접 노드 중 방문하지 않은 노드를 queue에 넣는다.
4. 2-3 반복

---

**Python**

```python
# BFS (너비 우선 탐색) 예제

from collections import deque
import sys

link = [[], [2, 3], [1, 3, 4, 5], [1, 2, 6, 7], [2, 5], [2, 4], [3, 7], [3, 6]]
visit = [0] * len(link)

def bfs(start):
    Q = deque()
    Q.append(start)
    visit[start] = True

    while Q:
        now = Q.popleft()
        sys.stdout.writelines(str(now) + '\n')
        for branch in link[now]:
            if not visit[branch]:
                visit[branch] = 1
                Q.append(branch)

bfs(1)
```



**C++**

```C++
#include <queue>
#include <vector>

using namespace std;

int number = 7;
int c[7];
vector<int> a[8];

void bfs(int start) {
  queue<int> q;
  q.push(start);
  c[start] = true;
  while(!q.empty()) {
    int x = q.front();
    q.pop();
    printf("%d ", x);
    for(int i = 0; i < a[x].size(); i++) {
      int y = a[x][i];
      if(!c[y]) {
        q.push(y);
        c[y] = true;
      }
    }
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

> BFS는 너비를 우선으로 하여 탐색한다는 특성이 중요하다.
>
> BFS 알고리즘 그 자체보다 다른 알고리즘에 많이 적용되는 점이 핵심이다.

