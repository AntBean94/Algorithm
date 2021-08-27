# BOJ 15566 개구리 1

'''
접근 방법
1번 음식
2번 취미
3번 가족
4번 철학

확인해야할 사항

1. 개구리별로 선호하는 연꽃에 배치하기
2. 통나무에서 대화가 가능한지 여부 파악하기

완전 탐색
vis 배열로 점유 여부 체크
불가능하다면 리턴

graph 확인

백트래킹 조건
1. 점유가 불가능한 경우
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
prog = [0] + [[0] + list(map(int, input().split())) for _ in range(N)]
pref = [0] + [list(set(map(int, input().split()))) for _ in range(N)]
graph = []
for i in range(M):
    graph.append(list(map(int, input().split())))

def check(vis):
    for i in graph:
        a = vis[i[0]]
        b = vis[i[1]]
        topic = i[2]
        if prog[a][topic] != prog[b][topic]:
            return False
    return True

# n: 개구리 번호, vis: 방문 배열 
def matching(n, vis):
    if n == N + 1:
        if check(vis):
            print('YES')
            print(*vis[1:])
            exit()
        return
    for i in pref[n]:
        if not vis[i]:
            vis[i] = n
            matching(n + 1, vis)
            vis[i] = 0
    return

vis = [0] * (N + 1)
matching(1, vis)
print('NO')