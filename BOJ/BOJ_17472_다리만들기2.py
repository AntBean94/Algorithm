# BOJ 17472 다리 만들기 2

'''
조건 
1. 다리는 바다에만 건설가능
2. 다리의 길이는 칸의 수
3. 다리의 방향이 바뀔 수 없다.
4. 다리의 길이는 2 이상
5. 다리의 끝은 땅이어야 한다.

6. 섬 A와 B를 연결하는 다리가 섬 C에 붙어있어도 연결된건 아님 
'''

# 모든 섬을 연결하는 다리 길이의 최솟값을 구해보자

# 접근 방법
# 1. 받은 데이터를 탐색
# 2. 각 섬에 번호를 메기고 1을 해당 섬의 번호로 바꾼다.
# 3. 섬의 번호는 2부터 시작한다.
# 4. 만들어진 배열로 노드의 갯수와 링크갯수를 판단한다.
# 5. 노드와 링크를 탐색하며 노드정보와 간선의 정보를 얻어낸다.
# 6. prim알고리즘을 통해서 최소거리를 측정한다.

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def make_num(y, x, num):
    box[y][x] = num
    for d in range(4):
        Y = y + dy[d]
        X = x + dx[d]
        if 0 <= Y < N and 0 <= X < M:
            if box[Y][X] == 1:
                make_num(Y, X, num)
#################################
# prim 알고리즘
def MST_Prim():
    key = [987654321] * (V+1)

    visited = [False] * (V+1)

    key[0] = 0

    # 간선의 갯수만큼 반복 (V-1)회
    for _ in range(V):
        min_idx = -1
        min_value = 987654321

        # 가중치가 가장 작은 노드를 T트리에 추가
        for i in range(V+1):
            if not visited[i] and key[i] < min_value:
                min_idx = i
                min_value = key[i]

        visited[min_idx] = True
        # 가중치가 가장 작은 노드를 기준으로 거리를 갱신
        for i in range(V+1):
            if not visited[i] and dist[min_idx][i] < key[i]:
                key[i] = dist[min_idx][i]
    
    if sum(key[:V]) >= 987654321:
        return -1
    else:
        return sum(key[:V])    
########################################
N, M = map(int, input().split())
box = []
for _ in range(N):
    line = list(map(int, input().split()))
    box.append(line)

# 노드와 간선정보 반환
num = 2
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            make_num(i, j, num)
            num += 1

# 노드의 갯수
V = num - 2
# 노드와 간선의 정보를 담을 리스트
dist = [[987654321] * (V+1) for _ in range(V+1)]

# 가로 탐색
for i in range(N):
    # 거리 초기화 해줘야 함
    dis = 0
    start = 0
    for j in range(M):
        if box[i][j] > 1:
            # 출발점이 있었고 현재와 다르다면
            if start and start != box[i][j]:
                # 최소 거리라면?
                if 1 < dis < dist[start-1][box[i][j]-1]:
                    dist[start-1][box[i][j]-1] = dist[box[i][j]-1][start-1] = dis
                    start = box[i][j]
            start = box[i][j]
            dis = 0
        elif box[i][j] == 0:
            dis += 1
# 세로 탐색
for j in range(M):
    dis = 0
    start = 0
    for i in range(N):
        if box[i][j] > 1:
            # 출발점이 있었고 현재와 다르다면
            if start and start != box[i][j]:
                # 최소 거리라면?
                if 1 < dis < dist[start-1][box[i][j]-1]:
                    dist[start-1][box[i][j]-1] = dist[box[i][j]-1][start-1] = dis
                    start = box[i][j]
            start = box[i][j]
            dis = 0
        elif box[i][j] == 0:
            dis += 1

# prim 알고리즘 통과
print(MST_Prim())