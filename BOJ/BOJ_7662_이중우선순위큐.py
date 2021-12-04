# BOJ 7662 이중 우선순위 큐

'''
queue 두개를 활용
하나는 max 
하나는 min

비어있음을 확인할 용도의 cnt 변수
pop은 check 리스트를 확인하며 죽어있는지 여부 확인

최종 연산 후 맥스큐의 최댓값, 민큐의 최솟값이 정답
'''

import heapq
import sys
input = sys.stdin.readline

def delete(queue, check):
    while True:
        n, id = heapq.heappop(queue)
        if check[id]:
            check[id] = 0
            return n

T = int(input())
for tc in range(T):
    k = int(input())
    check = {}
    id, cnt = 0, 0
    max_q = []
    min_q = []
    for i in range(k):
        cmd, n = input().split()
        n = int(n)
        if cmd == "I":
            heapq.heappush(max_q, (-n, id))
            heapq.heappush(min_q, (n, id))
            check[id] = 1
            cnt += 1
            id += 1
        else:
            if cnt == 0: continue
            if n == 1: delete(max_q, check)
            else: delete(min_q, check)
            cnt -= 1
    if cnt == 1: print(f"{delete(min_q, check)} " * 2)
    elif cnt > 1: print(-delete(max_q, check), delete(min_q, check))
    else: print("EMPTY")