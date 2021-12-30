# 문제 2

'''
완탐?

해가 정해져 있는 문제로
정답의 조합이 결정되어 있음

1: 3 3 1 0 3
3: 2 2 0 1 2
2: 1 1 1 0 1
3: 0 0 0 1 0

   4 2 2 1 4
3: 3 1 1 2 3
1: 2 2 0 1 2


돌 무더기: 8개
적정개수 최대 24개

정답을 정하고
해당 정답의 조합을 바꿔가며 가능한 케이스만 뽑아내기

백트래킹?

백트래킹 체크
1. 0이 둘 이상 => 아예 불가능
2. 0이 하나 => 그 수만 선택가능
3. 0이 없음 => 모든 케이스 가능


1. 메인 함수

2. 선택한 인덱스만 1더하고 나머지는 빼는 함수
- 배열조작 및 0갯수 반환

# 



'''
import sys
sys.setrecursionlimit(1000000)

def solution(stones, k):
    global answer
    global min_l
    answer = []
    min_l = 1000000
    L = len(stones)

    # 선택한 인덱스만 더하고 나머지는 1을 빼는 함수
    def move(arr, m):
        cnt = 0
        idx = []
        for j in range(L):
            if j == m: arr[j] += 1
            else:
                arr[j] -= 1
                # 0인 경우 cnt 증가
                if arr[j] == 0:
                    cnt += 1
                    idx.append(j)
        return cnt, idx

    # 되돌리는 함수
    def move_back(arr, m):
        for j in range(L):
            if j == m: arr[j] -= 1
            else: arr[j] += 1

    # 백트래킹
    def back_t(arr, route, l, r):
        global min_l
        if len(route) >= min_l: return
        for i in range(l, r):
            cnt, idx = move(arr, i)
            # 반환값에 따라 처리    
            if cnt == 0:
                back_t(arr, route + f"{i}", 0, L)
            elif cnt == 1:
                back_t(arr, route + f"{i}", idx[0], idx[0]+1)
            else:
                if cnt == L - 1 and arr[i] == k:
                    answer.append(route + f"{i}")
                    if len(route) + 1 < min_l: min_l = len(route) + 1
            move_back(arr, i)
        
    back_t(stones, "", 0, L)
    if not answer: answer = "-1"
    else: answer = sorted(answer)[-1]
    return answer


test_case = [
    [[1, 3, 2], 3],
    [[4, 2, 2, 1, 4], 1],
    [[5, 7, 2, 4, 9], 20]
]
for tc in test_case:
    print(solution(tc[0], tc[1]))

'''
정답

202
3213
-1
'''