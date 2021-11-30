# BOJ 2098 외판원 순회

'''
TSP(Trabeling Salesman problem)

완탐
def f(vis, depth):
    if depth == N: return

    for i in element:
        if not vis[i]:
            vis[i] = 1
            f(vis, depth + 1)
            vis[i] = 0
시간복잡도 N!

DP
각각의 노드로 끝나는 집합의 최소경로를 각각 기록
DP[vis 배열][현재 깊이]
vis배열길이 = 2 ^ 16
현재 깊이 = 16
한칸을 채우는데 16
시간복잡도 = 2^16 * 16^2 = 2^N * N^2

이후 다시풀기
'''
MAX = 100000000
N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]
ans = MAX

# 출발지 설정
s = 0
DP = [[MAX] * (2 ** N + 1) for _ in range(N - 1)]
pre = [[0] * (2 ** N + 1) for _ in range(N - 1)]
# 초기값 설정
for i in range(N):
    if i == s or not C[s][i]: continue
    DP[0][1<<i] = C[s][i]
    pre[0][1<<i] = i
# print(pre)
stack = []
# 출발점 고정 후 테이블 채우기
for i in range(N - 2):
    for j in range(1, 2 ** N + 1):
        d = pre[i][j]
        if DP[i][j] == MAX: continue
        # 방문기록이 없으면 최소값으로 갱신
        for k in range(N):
            if not i == N - 2 and k == s: continue
            if not C[d][k]: continue
            # print(d, k)
            if not (j & 1 << k):
                if DP[i][j] + C[d][k] < DP[i+1][j|1<<k]:
                    DP[i+1][j|1<<k] = DP[i][j] + C[d][k]
                    pre[i+1][j|1<<k] = k
                if i == N - 3:
                    stack.append([DP[i][j] + C[d][k], k])

# 도착지로 이동
# result = min(DP[N-1])
result = MAX
print(stack)
for a, b in stack:
    if not C[b][s]: continue
    if a + C[b][s] < result: result = a + C[b][s]
# print(result)
# result += C[pre[N-1][]][s]
for d in DP:
    print(d)

if result < ans: ans = result
print(ans)

'''
4
0 1 2 3
2 0 3 0
3 0 0 0
1 2 3 0
= 11

4
0 1 100 100
0 0 3 0
0 200 0 400
1 1 1 0
= 405

4
0 7 3 3
7 0 9 2
1 9 0 12
7 7 12 0
= 20
'''