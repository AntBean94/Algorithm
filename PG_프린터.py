# Programmers 스택/큐 프린터

from collections import deque

def solution(priorities, location):
    answer = 0
    cnt = 0

    Q = deque(priorities)
    while Q:
        # 뺀다.
        f = Q.popleft()
        location -= 1
        mx = f
        mx_idx = 0
        # 비교한다.
        for i in range(len(Q)):
            if Q[i] > mx:
                mx = Q[i]
                mx_idx = i
        # 뽑은값이 최댓값이라면
        if f == mx:
            cnt += 1
            # 뽑은값이 지정한 값이라면
            if location == -1:
                answer = cnt
                break
        # 뽑은값이 최댓값이 아니라면
        else:
            Q.append(f)
            if location < 0:
                location = len(Q) -1
            for i in range(mx_idx):
                s = Q.popleft()
                Q.append(s)
                location -= 1
                if location < 0:
                    location = len(Q) -1

    return answer


test_case = [
    [[2, 1, 3, 2], 2],
    [[1, 1, 9, 1, 1, 1], 0]
]
for tc in test_case:
    print(solution(tc[0], tc[1]))


'''후기
enumerate와 any를 사용했다면 훨씬 간단하게 짤수 있음
1. enumerate를 활용해 index를 포함한 큐를 만든다.
2. 큐가 비워질때까지 반복문
    2-1. pop
    2-2. pop한 값보다 큰값이 하나라도 있다면(any , for) append
    2-3. 없다면 answer += 1
        2-3-1. pop의 인덱스와 location이 같다면 리턴
'''