# 32 벨만-포드 알고리즘 (Bellman-Ford Algorithm)

'''
최단 경로 알고리즘 (음수 간선 포함)

일반적으로 음수 간선에 대한 최단경로는 다음과 같이 분류 가능
1. 모든 간선이 양수
2. 음수 간선이 존재
    - 음수 간선의 순환 X
    - 음수 간선의 순환 O

'벨만-포드' 알고리즘은 음의 간선이 포함된 상황에서도
사용할 수 있으며 '음수 간선의 순환'을 감지할 수 있다.
* 시간 복잡도 O(VE)

알고리즘
1. 출발 노드 설정
2. 최단 거리 배열 초기화
3. N번의 라운드 실행
    - 전체 간선 E를 하나씩 순회
    - 시작노드에서 각 간선을 거쳐 다른 노드로 가는 최단거리를 계산 및 배열 갱신
    - N + 1번째 라운드에서도 갱신이 일어난다면 '음수 간선의 순환 O'

벨만-포드 VS 다익스트라
1. 다익스트라
    - 매번 방문하지 않은 노드중에서 최단거리가 가장 짧은 노드를 선택
    - 음수 간선이 존재하지 않는 경우 최적해를 찾을 수 있다.
    - 시간복잡도: O(NlogN) - 힙을 사용한 경우

2. 벨만-포드
    - 매번 모든 간선을 전부 확인
      따라서, 다익스트라 알고리즘에서의 최적의 해를 항상 포함
    - 음수 간선의 순환을 감지 가능
    - 시간복잡도: O(VE) - 다익스트라보다 느리다.
    
'''


# N: 정점의 갯수, M: 간선의 갯수
N, M = map(int, input().split())
INF = 1000000000
dist = [INF] * (N + 1)
graph = [('start 노드', 'end 노드', 'cost 비용')]

def bellman_ford(start):
    # 자신까지의 거리는 0
    dist[start] = 0
    # 시작점을 기준으로 (N-1)번의 라운드 실행
    for i in range(N):
        # M개의 간선을 확인
        for j in range(M):
            now = graph[j][0]
            nxt = graph[j][1]
            cost = graph[j][2]
            # start에서 now를 거쳐 nxt로 가는 최단거리가 갱신 가능한지 확인
            # 즉 j번 간선을 거쳐서 최단거리를 갱신할 수 있는지 확인
            if dist[now] != INF and dist[now] + cost > dist[nxt]:
                dist[nxt] = dist[now] + cost
                # N 번째에도 갱신이 이루어진다면 음수 순환이 있다는 의미
                if i == N - 1:
                    return True
    return False