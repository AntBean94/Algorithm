# BOJ 12100 2048(Easy)

'''
5번 이동

경우의 수 = 4 ^ 5 = 1,024가지
보드 판 = 400

400 * 1024 = 약 40만
=> 완탐

삼성 기출이므로 sys 함수 사용 X

중요한 포인트
1. 수를 붙이고 나눌 때 좌표를 기록하는 방식
- 수를 붙일 때
큐에 하나씩 넣는다.
cnt를 센다.
결합이 발생할 때 큐에서 값을 하나 빼고 cnt 1 증가 후 좌표에 부여
결합이 발생하지 않았다면 큐에서 하나씩 빼면서 cnt 1증가시키고 좌표에 부여

- 수를 나눌 때
현재 큐에서 값을 뽑아 0으로 만든다.
이전값이 기록된 큐에서 하나씩 빼 값을 채운다.

2. 결합할 수를 찾고 결합하는 방식
- 결합 할 수를 찾는 방식
  큐를 사용한다

=> 방향을 정하며 완전탐색(재귀호출)하는 메인 함수
=> 정해진 방향대로 값을 옮기고 이전 위치와 바뀐 위치를 반환하는 함수

=> 현재 상태를 나타내는 큐는 관통
=> 이전값을 기록하는 큐는 계층마다 존재

[value, y, x]

4 0 4 0
0 0 0 0
4 0 4 0
0 0 0 0

d = 0 인 경우 (x축 기준 정렬, 앞에서부터 탐색, cnt = 0 시작)
[
    [4, 0, 0],
    [4, 2, 0],
    [4, 0, 2],
    [4, 2, 2]
]

d = 1 인 경우 (y축 기준 정렬, 뒤에서부터 탐색, cnt = N - 1 시작)
[
    [4, 0, 0],
    [4, 0, 2],
    [4, 2, 0],
    [4, 2, 2]
]

d = 2 인 경우 (x축 기준 정렬, 뒤에서부터 탐색, cnt = N - 1 시작)
d = 3 인 경우 (y축 기준 정렬, 앞에서부터 탐색, cnt = 0 시작)

0 2 4
0 4 8
0 8 16

'''


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
status = []
start = [-1, N, N, -1]
move_idx = [1, -1, -1, 1]
axis = [2, 1, 2, 1]
hor = [1, 2, 1, 2]

def move_num(arr, d):
    new_arr = []
    # 정렬
    # 위 또는 아래 방향인 경우
    if d == 0 or d == 2:
        arr.sort(key=lambda x: x[2])
    # 좌 또는 우 방향인 경우
    else:
        arr.sort(key=lambda x: x[1])

    # 하나씩 뽑아서 변환
    cnt = start[d]
    queue = []
    # 여기서부터 중요
    for a in arr:
        # 큐가 비어있다면 채운다.
        if not queue: queue.append(a)
        # 비어있지 않다면 가장 마지막 값과 비교
        else:
            last = queue[-1]
            # 같은 축을 공유한다면
            if a[axis[d]] == last[axis[d]]:
                # 값이 같다면 합치고 뺀다.
                if a[0] == last[0]:
                    queue = []
                    new = [a[0] * 2, a[1], a[2]]
                    cnt += move_idx[d]
                    new[hor[d]] = cnt
                    new_arr.append(new)
                # 값이 다르다면 앞에있는 값을 빼고 new에 넣는다.
                else:
                    new = queue.pop()
                    cnt += move_idx[d]
                    new[hor[d]] = cnt
                    new_arr.append(new)
                    queue.append(a)

            # 같은 축을 공유하지 않는다면
            else:
                # 기존 큐를 비우면서 좌표를 새로 부여하고 new에 넣는다.
                new = queue.pop()
                cnt += move_idx[d]
                new[hor[d]] = cnt
                new_arr.append(new)
                # cnt 초기화
                cnt = start[d]
                # 새로운 값을 큐에 넣는다.
                queue.append(a)

    # 큐에 값이 남아있다면 처리
    if queue:
        new = queue.pop()
        cnt += move_idx[d]
        new[hor[d]] = cnt
        new_arr.append(new)

    return new_arr

# 보드가 꼭 필요할까?
def main_game(board, status, k, route):
    global ans
    # if route == '1':
    #     print(status)
    print(status, route)
    if k == 1:
        # 최댓값 갱신
        max_val = sorted(status, reverse=True)[0][0]
        if max_val > ans:
            ans = max_val
        return
    
    # 완전 탐색
    for d in range(4):
        # 값 변경
        new_status = move_num(status, d)
        # 재귀 호출(빠져나오면서 다시 바뀜)
        main_game(board, new_status, k + 1, route + str(d))


# 초기 좌표 등록
for i in range(N):
    for j in range(N):
        if board[i][j]:
            status.append([board[i][j], i, j])

route = ""
main_game(board, status, 0, route)
print(ans)