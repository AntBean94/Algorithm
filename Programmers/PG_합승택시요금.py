# Programmers 합승 택시 요금

def solution(n, s, a, b, fares):
    answer = 10000000000
    # 플로이드 워셜
    # 거리 초기화
    INF = 1000000000
    d = [[INF] * (n + 1) for _ in range(n + 1)]
    for x, y, fare in fares:
        d[x][y] = fare
        d[y][x] = fare
    for i in range(1, n + 1):
        d[i][i] = 0

    # 각 정점을 기준으로 거리 최소화
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]

    for i in range(1, n + 1):
        cost = d[s][i] + d[i][a] + d[i][b]
        if cost < answer:
            answer = cost
    return answer


test_case = [
    [6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]],
    [7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]],
    [6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]]
]
for n, s, a, b, fares in test_case:
    print(solution(n, s, a, b, fares))
    print()