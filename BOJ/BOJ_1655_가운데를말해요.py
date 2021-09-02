# BOJ 1655 가운데를 말해요

'''
우선순위 큐 두개를 만든다.
하나는 최대힙(A), 하나는 최소힙(B)

N(A) - N(B) <= 1 를 유지하도록
각각의 우선순위 큐에서 값을 pop, push한 뒤 mid값을 수정
'''

import heapq
import sys
input = sys.stdin.readline

N = int(input())
A = []
B = []
alen = 0
blen = 0
mid = 0
for i in range(N):
    n = int(input())
    # 가장 처음 값은 중간값
    if i == 0: mid = n 
    # 중간값보다 작다면 A에 넣기
    elif n < mid: 
        heapq.heappush(A, -n)
        alen += 1
    # 중간값보다 크거나 같다면 B에 넣기
    else: 
        heapq.heappush(B, n)
        blen += 1
    
    # 길이 체크를 통해 중간값 변경
    if alen > blen:
        heapq.heappush(B, mid)
        mid = -heapq.heappop(A)
        alen -= 1
        blen += 1
    elif blen > alen + 1:
        heapq.heappush(A, -mid)
        mid = heapq.heappop(B)
        alen += 1
        blen -= 1
    # 출력
    print(mid)