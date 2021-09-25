# 시나리오 2

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
problem = 2

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
    1. 바로 매칭 시켜주기
    2. 매칭결과에 따라 등급 바꾸기
        => 기본 등급: 승률에 따라 조정
    3. 승률이 유사한 유저끼리 매칭
    
    '''

    user_info = {i: [0,0] for i in range(1, 901)}

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
            score = 9250
            user_info = sorted(user_info.items(), key=lambda x:x[1][0] / (x[1][0] + x[1][1]), reverse=True)
            for user, data in user_info:
                grade.append({'id': user, 'grade': score})
                score -= 10
            print(user_info)
            print(grade)
            api.change_grade(BASE_URL, headers, grade)
        print(user_info)

    api.get_score(BASE_URL, headers)



    

# 메인 함수 실행
if __name__ == '__main__':
    # 메인 프로그램으로서 실행 ...
    main()