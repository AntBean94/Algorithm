# BOJ 2342 Dance Dance Revolution

'''
수열의 길이: 100,000

중앙 => 외각: 2
외각 => 인접: 3
외각 => 반대: 4
현재 => 현재: 1

발위치 조합: 5 P 2 = 20 가지

예제
(0, 0)
(1, 0), (0, 1) 2
(2, 0), (2, 1), (1, 2), (0, 2) 각 위치로 갈 수 있는 최솟값을 갱신

하나씩 순회하면서 
해당 위치가 없다면 추가
있다면 적은값으로 갱신

'''

P = {
    0: [1, 2, 2, 2, 2],
    1: [3, 1, 3, 4, 3],
    2: [3, 3, 1, 3, 4],
    3: [3, 4, 3, 1, 3],
    4: [3, 3, 4, 3, 1]
}

A = list(map(int, input().split()))
if A[0]: T = [{(0, A[0]): 2, (A[0], 0): 2}]
else: 
    print(0)
    exit()

for i in range(1, len(A)-1):
    n = A[i]
    # 칸 추가
    T.append(dict())
    # 이전칸 순회하며 n에 해당하는 비용 갱신
    for key, value in T[i-1].items():
        # n과 key값에 포함되면 제자리 이동만 가능
        if n in key:
            # 현재칸에 존재여부에 따라
            if key in T[i]: T[i][key] = min(T[i-1][key] + 1, T[i][key])
            else: T[i][key] = T[i-1][key] + 1
        # 존재하지 않는 경우(2가지 케이스)
        else:
            # 다음 발 위치 키
            for k in range(2):
                y, x = key[k], key[(k+1)%2]
                if not k: new_key = (n, x)
                else: new_key = (x, n)
                # 현재 칸에 존재여부에 따라
                if new_key in T[i]: T[i][new_key] = min(value + P[y][n], T[i][new_key])
                else: T[i][new_key] = value + P[y][n]
print(min(T[-1].values()))