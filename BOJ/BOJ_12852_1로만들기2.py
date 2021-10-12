# BOJ 12852 1로 만들기 2

'''
다이나믹 프로그래밍

table = [0, 2, 1, 1, 0, 1, 0]
0, 1, 2, 3, 4, 5, 6

'''
N = int(input())
T = [0] * (N + 1)
R = [i for i in range(N+1)]
for i in range(N, 1, -1):
    if not i == N and not T[i]: continue
    # 3으로 나뉘는 경우
    if not i % 3:
        j = i // 3
        if T[j] and T[i] + 1 < T[j]: T[j], R[j] = T[i] + 1, i
        elif not T[j]: T[j], R[j] = T[i] + 1, i
    # 2로 나뉘는 경우
    if not i % 2:
        j = i // 2
        if T[j] and T[i] + 1 < T[j]: T[j], R[j] = T[i] + 1, i
        elif not T[j]: T[j], R[j] = T[i] + 1, i
    j = i - 1
    if T[j] and T[i] + 1 < T[j]: T[j], R[j] = T[i] + 1, i
    elif not T[j]: T[j], R[j] = T[i] + 1, i
print(T[1])
# 경로 찾기
s = 1
arr = [1]
while s != N:
    s = R[s]
    arr.append(s)
print(*arr[::-1])