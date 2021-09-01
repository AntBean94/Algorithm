# Programmers 광고 삽입

'''
접근 방법
0. 전체 시청구간을 배열로 만든다.
- 단위는 '초'
- 총 길이 = HH * 3600 + MM * 60 + SS + 1

1. 로그의 시작과 끝을 배열에 저장
- 1번 기록부터 id값을 준다.
- 중첩되는 값은 2차원 리스트 형태로 값 추가

2. 투포인터로 구간합 구하기
- 해시를 이용해 각 id값을 더하고 빼준다.
- 그렇게 누적합을 구하면 됨
- 현재 총 값이 몇개인지 cnt에 담고 해당 값만큼 전체 시청기간에 추가
- 최대값을 수정한다.

전체 구간: 360,000 (N)
로그: 300,000 (M)

시간복잡도: O(N + M)

'''

def solution(play_time, adv_time, logs):
    answer = ''
    # 0. 전체 시청 구간을 배열로 만든다.
    h, m, s = map(int, play_time.split(":"))
    time_per_s = h * 3600 + m * 60 + s + 1
    timeline = [list() for _ in range(time_per_s)]

    # 1. 로그의 시작과 끝을 배열에 저장
    id = 0
    check = {}
    for log in logs:
        id += 1
        check[id] = 0
        # 시작, 끝값 추출(초 단위)
        start, end = log[:8], log[9:]
        h1, m1, s1 = map(int, start.split(':'))
        h2, m2, s2 = map(int, end.split(':'))
        start = h1 * 3600 + m1 * 60 + s1
        end = h2 * 3600 + m2 * 60 + s2
        # 시작위치와 끝 위치에 id값 추가
        timeline[start].append(id)
        timeline[end].append(id)
    
    # 2. 구간 합 구하기
    # 시작 구간 합
    play_time = 0
    play_cnt = 0
    hh, mm, ss = map(int, adv_time.split(':'))
    adv_s = hh * 3600 + mm * 60 + ss
    time_cnt = []
    for s in range(adv_s):
        for i in timeline[s]:
            if not check[i]:
                check[i] = 1
                play_cnt += 1
            else:
                check[i] = 0
                play_cnt -= 1
        play_time += play_cnt
        time_cnt.append(play_cnt)
    max_time = play_time
    answer = 0
    # 구간합 변경하기
    for s in range(time_per_s - adv_s):
        l, r = s, s + adv_s
        # 더하기
        for i in timeline[r]:
            if not check[i]:
                check[i] = 1
                play_cnt += 1
            else:
                check[i] = 0
                play_cnt -= 1
        play_time += play_cnt
        time_cnt.append(play_cnt)
        # 빼기
        play_time -= time_cnt[l]
        # 최대값 체크
        if play_time > max_time:
            max_time = play_time
            answer = l + 1

    # 초 => 시간 변환
    H = str(answer // 3600)
    answer %= 3600
    M = str(answer // 60)
    answer %= 60
    S = str(answer)
    if len(H) == 1: H = "0" + H
    if len(M) == 1: M = "0" + M
    if len(S) == 1: S = "0" + S
    answer = f'{H}:{M}:{S}'
    return answer



test_case = [
    ["02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]],
    ["99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]],
    ["50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]]
]
for tc in test_case:
    print(solution(tc[0], tc[1], tc[2]))