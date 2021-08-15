# 23강 이분 매칭

## Bipartite Matching

#### A 집단이 B 집단을 선택하는 방법에 대한 알고리즘

---

1. 초기값 세팅
   - 각 도착 노드의 방문여부를 체크하는 리스트
   - 각 도착 노드의 점유 노드를 체크하는 리스트
   - 그래프
2. 시작 노드로 반복문 실행
   - 각 도착 노드 방문여부 초기화(False)
   - dfs 실행
3. dfs
   - 각 도착노드의 방문상태 확인
   - 방문하지 않았다면 방문 체크
   - 방문노드에 점유노드가 없거나 점유노드가 다른 노드로 갈 수 있다면(재귀)
     - 점유노드를 현재 출발노드로 변경
     - return
   - return
4. 결과 출력

---

**Python**

```python
# 23강 이분 매칭 (Bipartite Matching) 예제

'''
예제

3 3 5
1 1
1 2
1 3
2 1
3 2

'''

import sys
input = sys.stdin.readline

# 초기값 세팅
S, N, M = map(int, input().split())
visit = [False] * (N + 1)
occupy = [0] * (N + 1)
graph = [[] for _ in range(S + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# 매칭에 성공한 경우 True, 실패한 경우 False 반환
def dfs(x):
    # 연결된 모든 노드에 대해서 점유 시도
    for i in range(len(graph[x])):
        y = graph[x][i]
        # 이미 처리된 노드(재귀 내에서)는 생략
        if visit[y]: continue
        visit[y] = True
        # 점유 노드가 없거나, 이미 점유한 노드가 다른곳으로 이동 가능하다면
        if occupy[y] == 0 or dfs(y):
            occupy[y] = x
            return True
    return False

cnt = 0
# 모든 출발 노드에 대해서 반복
for i in range(1, S + 1):
    # 도착 노드 방문여부 초기화
    for j in range(N + 1):
        visit[j] = False
    if dfs(i): cnt += 1

print(f'{cnt}개의 매칭이 이루어졌습니다.')
for i in range(1, len(occupy)):
    print(f'{i} -> {occupy[i]}')
```



**C++**

```C++
#include <iostream>
#include <vector>
#define MAX 101

using namespace std;

vector<int> a[MAX];
int d[MAX];
bool c[MAX];
int n = 3, m;

bool dfs(int x) {
  for(int i = 0; i < a[x].size(); i++) {
    int t = a[x][i];
    if(c[t]) continue;
    c[t] = true;
    if(d[t] == 0 || dfs(d[t])) {
      d[t] = x;
      return true;
    }
  }
  return false;
}

int main(void) {
  a[1].push_back(2);
  :
  :
  :
  a[3].push_back(2);
  int count = 0;
  for(int i = 1; i <= n; i++) {
    fill(c, c + MAX, false);
    if(dfs(i)) count++;
  }
  printf('%d 개의 매칭이 이루어졌습니다.\n', count);
}
```



## 정리

시간 복잡도: O(E * V)