from math import ceil

def solution(n, stations, w):
    answer = 0
    width = w * 2 + 1
    # 초깃값
    answer += ceil(max(0, stations[0] - w - 1) / width)
    # 이후값
    for i in range(1, len(stations)):
        answer += ceil(max(0, stations[i] - stations[i-1] - 2 * w - 1) / width)
    # 마지막값
    answer += ceil(max(0, n - stations[-1] - w) / width)
    print(answer)
    return answer

test_case = [
    [11, [4, 11], 1],
    [16, [9], 2],
    [10, [1,2,5,6,7,8,9], 1]
]
for tc in test_case:
    solution(tc[0], tc[1], tc[2])

'''
N이 2억?
stations는 최대 1만개
W는 만 이하의 자연수

각 차이의 몫을 구하면 된다.
9라면 

7 - 0을 5로 나누고 몫

9 - 0

'''