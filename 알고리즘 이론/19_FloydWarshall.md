# 19강 플로이드 와샬

## Floyd Warshall

## ''거쳐가는 정점'을 기준으로 최단 거리를 구하는 것

---

"거쳐가는 정점을 기준으로 사용하기 위해 3중 for문을 활용한다."

1. 거리 정보를 받는다.
2. 거쳐가는 정점을 기준으로 for 반복문 실행
3. 시작점 - 종료점 vs 시작점 - 거쳐가는 점 - 종료점
4. 더 작은점을 거리배열에 저장한다.
5. 마지막까지 반복

---

**Python**

```python
# 19강 플로이드 와샬 (Floyd Warshall) 예제

INF = 100000000

# 거리정보 초기화
a = [
    [0, 5, INF, 8],
    [7, 0, 9, INF],
    [2, INF, 0, 4],
    [INF, INF, 3, 0]
]
N = len(a)

def floydWarshall():
    # 최단거리 초기화
    d = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            d[i][j] = a[i][j]
    # k를 거치는
    for k in range(N):
        # 출발지점(i)과 도착지점(j)
        for i in range(N):
            for j in range(N):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]

    return d

ans = floydWarshall()

for i in range(N):
    print(*ans[i], end="\n")
```



**C++**

```C++
#include <stdio.h>

int number = 4;
int INF = 1000000000;

// 자료 배열을 초기화 한다.
int a[4][4] = {
  {0, 5, INF, 8},
  {7, 0, 9, INF},
  {2, INF, 0, 4},
  {INF, INF, 3, 0}
};

void floydWarshall() {
  // 결과 그래프를 초기화 한다.
  int d[number][number];
  
  for(int i = 0; i < number; i++) {
    for(int j = 0; j < number; j++) {
      d[i][j] = a[i][j];
    }
  }
  
  // k = 거쳐가는 노드
  for(int k = 0; k < number; k++) {
    // i = 출발 노드
    for(int i = 0; i < number; i++) {
      // j = 도착 노드
      for(int j = 0; j < number; j++) {
        if(d[i][k] + d[k][j] < d[i][j]) {
          d[i][j] = d[i][k] + d[k][j];
        }
      }
    }
  }
  // 결과를 출력한다.
  for(int i = 0; i < number; i++) {
    for(int j = 0; j < number; j++) {
      printf("%d ", d[i][j]);
    }
    printf("\n");
  }
}

int main(void) {
  floydWarshall();
}
```

