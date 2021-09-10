# Programmers 오픈채팅방

'''
해시를 활용해서 고유의 id값을 주면 된다.
1. 정보를 하나씩 탐색
2. enter, leave 명령어의 경우 배열에 [명령, uid]를 저장
3. change 명령어의 경우 hash값에 있는 아이디를 바꿔준다.
4. 정보 확인이 끝나면 배열에서 정보를 "**님이 들어왔습니다."형식으로 바꿔준다.
'''

def solution(record):
    answer = []
    N = len(record)
    user_info = {}
    logs = []
    # 정보 순회
    for n in range(N):
        info = list(map(str, record[n].split()))
        cmd, uid = info[0], info[1]
        if cmd == "Enter" or cmd == "Leave":
            logs.append([cmd, uid])
            if cmd == "Enter": user_info[uid] = info[2]
        else: user_info[uid] = info[2]
    
    # 로그 => 평문 전환
    for cmd, uid in logs:
        if cmd == "Enter":
            answer.append(f"{user_info[uid]}님이 들어왔습니다.")
        else:
            answer.append(f"{user_info[uid]}님이 나갔습니다.")
    return answer



test_case = [
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
]
for tc in test_case:
    print(solution(tc))