# BOJ 5569 출근 경로 - dfs(시간초과)

'''
그래프 탐색?

처음에 출발했을때는 방향 바로 바꾸기 가능

그 뒤로 방향을 바꿧다면 2칸 이후부터 가능

3 4 일때
가로길, 세로길
[2, 3]

def dfs([우, 상], 이전 방향, 이전 길이):
    1. 탈출조건
    상, 우 둘다 비어있다면 1추가

    2. 숫자 정보
    for i in range(2):
        우(0), 상(1) 한번씩 돌기
        if 이전방향 != 현재방향:
            if 길이 < 2:
                continue
            else:
                if 방향[i]:
                    방향[i] -= 1
                    dfs(방향, i, 1)
                    방향[i] += 1
        if 방향[i]:
            방향[i] -= 1
            dfs(방향[], i, 길이 + 1)
            방향[i] += 1


for i in range(2):
    dfs([], i, 3)

'''

import sys
input = sys.stdin.readline

def dfs(arr, dir, k):
    global cnt
    # 탈출 조건
    if not(arr[0] or arr[1]):
        cnt += 1
        # print(cnt)
        return
    
    for d in range(2):
        # 방향이 다르다면
        if dir != d:
            if k < 2:
                continue
            else:
                if arr[d]:
                    arr[d] -= 1
                    # print(f'배열: {arr}, 방향: {d}, 길이: {k}')
                    dfs(arr, d, 1)
                    arr[d] += 1
        # 방향이 같다면
        else:
            if arr[d]:
                arr[d] -= 1
                # print(f'배열: {arr}, 방향: {d}, 길이: {k}')
                dfs(arr, d, k+1)
                arr[d] += 1

arr = list(map(int, input().split()))
arr[0] -= 1
arr[1] -= 1

cnt = 0

for i in range(2):
    arr[i] -= 1
    dfs(arr, i, 3)
    arr[i] += 1
print(cnt % 100000)