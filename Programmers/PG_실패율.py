# Programmers 실패율

'''
실패율 = 스테이지에 도달했으나 이직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수

스테이지를 클리어한 플레이어의 수 = 이후 스테이지를 플레이하고 있는 플레이어의 합

즉, 스테이지에 도달한 플레이어의 수
= 이후 스테이지 플레이어 수 + 현재 스테이지 플레이중인 유저의 수

'''
import heapq

def solution(N, stages):
    answer = []

    def check(info, s):
        for i in range(N + 1):
            if i < s:
                info[i][1] += 1
            else:
                info[i][0] += 1
                break

    info = [[0, 0] for _ in range(N + 2)]
    # 스테이지 정보 입력
    for s in stages:
        check(info, s)
    
    Q = []
    # 실패율 계산
    for i in range(1, N + 1):
        if sum(info[i]) == 0: heapq.heappush(Q, [0, i])
        else: 
            pri = info[i][0] / sum(info[i])
            heapq.heappush(Q, [-pri, i])
    
    # 실패율 순서대로 뽑기
    for i in range(1, N + 1):
        answer.append(heapq.heappop(Q)[1])

    return answer

test_case = [
    [5, [2, 1, 2, 6, 2, 4, 3, 3]],
    [4, [4,4,4,4,4]]
]
for tc in test_case:
    print(solution(tc[0], tc[1]))