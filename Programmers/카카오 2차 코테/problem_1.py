# 시나리오 1
# 4e95b8

import api
import json

# auth token 불러오기
with open('./secrets.json', 'r') as f:
    token_data = json.load(f)

# API URL
BASE_URL = "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"
content_type = 'application/json'
headers = {
    'X-Auth-Token': token_data['X-Auth-Token'],
    'Content-Type': content_type
}
problem = 1

# 0. 게임 설명
'''
---------- 매칭 목표 ----------
1. 정확도 
- 각 유저가 원래 갖고 있는 고유실력으로 정렬한 결과 = 부여된 등급을 기준으로 정렬 (최대한 유사하도록)
- 유저간 매칭을 성사시키고 결과에 따라 등급을 부여하는 방식
2. 효율성
- 유저 대기시간을 최소화하기

---------- 제한 사항 ----------
1. 유저
- 같은 실력을 가진 두 유저는 존재하지 않는다.(무승부 X)
- 1,000 <= 실력 <= 100,000
- 실력 분포: (평균 = 40,000), (표준편차 = 20,000)
- z = (유저 실력 - 평균) / 표준편차
=> z > 1: 상위 30% 
=> z > 2: 상위 95%
=> z > 3: 상위 99%

- 매칭 신청후 최대 대기시간: 15분
- 취소 후 바로 재신청 가능
- 고유 ID를 가지고 있음

2. 게임
- 1:1
- 중단, 포기, 무승부 X
- 시나리오1) 일부러 지는 경우 없음
- 시나리오2) 일부러 지는 경우 있음(어뷰저)
- 게임에 걸리는 시간(확률): 실력차 가중치(적을수록 오래, 클수록 빠르게 끝남)
    t = 40분 - (실력차 / 99000 * 35) + e(-5 <= e <= 5)
    3 <= t <= 40 (범위를 초과하면 경계값 반영, 분 단위)
- 승부 결과(확률): 실력이 높은 유저가 이길 확률이 높음
    A가 이길 확률(p) = (A실력) / (A실력 + B실력)

3. 매칭
- 대기열 유저의 중복 신청 없음
- 게임 도중 매칭 신청 없음
- 게임 종료시각 = 매칭 신청시각 가능
- 게임 시작하면 대기열에서 제외

---------- 시나리오 ----------
시나리오 1.
- 매칭을 1회 이상 신청하는 유저의 수: 30명
- 매칭 신청 빈도: 분당 평균 1건

시나리오 2.
- 900명
- 평균 45건

어뷰저
- 자신보다 실력이 낮은 유저 상대로 80%확률로 패배/ 10분 이하
- 20%확률로 승리하는경우에는 일반적인 게임과 동일
- 비율: 5%
- 시간: 3 ~ 10분
- 어뷰저간의 승부에서는 실력이 낮은 어뷰저는 정상 플레이

---------- 점수 ----------
1. 3개의 스코어
2. 등급 정렬 정확도, 매칭 정확도, 대기 시간 효율성

---------- API ----------
총 540분(540턴)
0. start
1. waiting line api
2. match api
- 매칭 시킬 유저가 없어도 실행(그래야 다음턴으로 넘어감)
- 0 ~ 540턴까지 매칭 신청 가능
- 이후 신청 X
- 555턴 까지 대기 가능(마지막 매칭 유저 결과 40분 걸릴수있음)
- 595턴까지 결과를 확인해야 함

3. game result api
4. change grade api
5. user info api
6. score api

'''
# ============================ 메인 알고리즘 ============================== #
def main():

    # 시나리오 시작
    res = api.start(BASE_URL, headers, problem)
    headers['Authorization'] = res['auth_key']
    
    # api 테스트
    '''
    api.waiting_line(BASE_URL, headers)
    {
        "waiting_line": [
            { "id": 1, "from": 3 },
            { "id": 2, "from": 14 },
            ...
        ]
    }
    api.game_result(BASE_URL, headers)
    {
        "game_result": [
            {"win": 10, "lose": 2, "taken": 7 },
            {"win": 7, "lose": 12, "taken": 33 },
            ...
        ]
    }
    api.user_info(BASE_URL, headers)
    {
        "user_info": [
            { "id": 1, "grade": 2100 },
            { "id": 13, "grade": 1501 },
            ...
        ]
    }
    api.match(BASE_URL, headers, [[1, 2], [2, 3]])
    [[][]]
    api.change_grade(BASE_URL, headers, [{'id': 1, 'grade': 1000}])
    [{}, {}]
    api.get_score(BASE_URL, headers)
    '''

    # 시나리오(1) 전략
    '''
    첫 번째 전략(승률)
    1. 바로 매칭 시켜주기
    2. 무작위 매칭
    - 비슷한 유저끼리 매칭을 하게 되면 승률의 신뢰도가 하락함
    3. 최종 승률에따라 등급결정
    시나리오 1) score = 210.11 (60/49/99.9)
    시나리오 2) score = 196.48 (58/54/77)

    두 번째 전략(레이팅 시스템)
    1. elo 레이팅 참조
    2.     
    '''

    user_info = {i: [0,0] for i in range(1, 31)}

    for i in range(596):
        # 경기 결과
        res = api.game_result(BASE_URL, headers)
        for game in res["game_result"]:
            winner = game["win"]
            loser = game["lose"]
            user_info[winner][0] += 1
            user_info[loser][1] += 1
        
        match_arr = []
        if i <= 540:
            res = api.waiting_line(BASE_URL, headers)
            tmp = []
            for user in res['waiting_line']:
                key = user['id']
                if len(tmp) < 2: 
                    tmp.append(key)
                    if len(tmp) == 2: match_arr.append(tmp)
                else: 
                    match_arr.append(tmp)
                    tmp = [key]
        api.match(BASE_URL, headers, match_arr)
        if i == 594:
            grade = []
            # 등급 범위 0 ~ 9999
            score = 7000
            user_info = sorted(user_info.items(), key=lambda x:x[1][0] / (x[1][0] + x[1][1]), reverse=True)
            for user, data in user_info:
                grade.append({'id': user, 'grade': score})
                score -= 150
            print(user_info)
            print(grade)
            api.change_grade(BASE_URL, headers, grade)
        print(user_info)

    api.get_score(BASE_URL, headers)



    

# 메인 함수 실행
if __name__ == '__main__':
    # 메인 프로그램으로서 실행 ...
    main()