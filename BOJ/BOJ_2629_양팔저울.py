# BOJ 2629 양팔저울

'''
추의 갯수는 30개
추의 무게는 최대 500g
=> 총 무게는 15,000

가능한 모든 경우의 수를 측정하라는 것

확인할 구슬의 갯수는 7개

구슬 무게는 40,000보다 작거나 같은 자연수

1, 3, 5

1, 3, 2, 4 가능

1, 3, 5, 4, 6, 8, 2, 7, 9
즉, 각 케이스에 +,- 경우를 모두 추가

큰수에서 작은수를 뺀것과 서로 더한 것

'''
import sys
input = sys.stdin.readline

N = int(input())
W = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

table = [0] * 40001
table[W[0]] = 1

for i in range(1, N):
    w = W[i]
    vis = [0] * 40001
    for j in range(40000, -1, -1):
        # 기존 무게
        if not table[j] or vis[j]: continue
        # 더한값 추가
        a, b = w + j, abs(w - j)
        if not table[a]: vis[a] = 1
        if not table[b]: vis[b] = 1
        table[w + j] = 1
        table[abs(w - j)] = 1
    table[w] = 1

for i in range(M):
    if table[B[i]]: print("Y", end=" ")
    else: print("N", end=" ")
