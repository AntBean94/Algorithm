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

0 0 0 0 
0 0 0 0
0 0 0 0 
0 0 0 0

'''


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
status = []

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
    cnt = 0
    
    

    return new_arr

# 보드가 꼭 필요할까?
def main_game(board, status, k):
    global ans
    if k == 5:
        # 최댓값 갱신
        max_val = sorted(status, reverse=True)[0][0]
        if max_val > ans:
            ans = max_val
    
    # 완전 탐색
    for d in range(4):
        # 값 변경
        new_status = move_num(status, d)
        # 재귀 호출(빠져나오면서 다시 바뀜)
        main_game(board, new_status, k + 1)


# 초기 좌표 등록
for i in range(N):
    for j in range(N):
        if board[i][j]:
            status.append([board[i][j], i, j])

main_game(board, status, 0)