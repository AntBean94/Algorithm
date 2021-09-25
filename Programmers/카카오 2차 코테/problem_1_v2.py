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

# ============================ 메인 알고리즘 ============================== #
def main():

    # 시나리오 시작
    res = api.start(BASE_URL, headers, problem)
    headers['Authorization'] = res['auth_key']

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
    1. 유저 기본등급 부여(평균 4950)
    2. 대기 리스트 확인
        - waiting api 호출
        - user api 호출
    3. 등급이 비슷한 유저끼리 매칭
    4. 매칭 결과 수령
        - 두 유저의 예상 승률 계산| W.e = A/(A+B))
        - 두 유저의 점수 증감| P.after = P.before + K * (W - W.e)
        - K: 가중치, W = 1 or 0(승리시 1, 패배시 0), W.e = 예측 승률
        - K 값 결정 => 걸리는 시간 반영
    '''

    # 1. 유저 기본 등급 부여
    grade = {i : 4950 for i in range(1, 31)}
    md_grade = [{"id": i, "grade": 4950} for i in range(1, 31)]
    api.change_grade(BASE_URL, headers, md_grade)
    

    for i in range(596):
        # 결과 확인
        result = api.game_result(BASE_URL, headers)
        # 점수 조정
        md_grade = []
        for case in result["game_result"]:
            winner = case["win"]
            loser = case["lose"]
            time = case["taken"]

            # 예측 승률 계산
            w_grade = grade[winner]
            l_grade = grade[loser]
            W_w = 1 / (10 ** ((l_grade - w_grade)/4950 + 1))
            W_l = 1 / (10 ** ((w_grade - l_grade)/4950 + 1))
            # W_w = w_grade / (w_grade + l_grade)
            # W_l = l_grade / (l_grade + w_grade)

            # 결과 반영
            K = 30 * 40 / time
            grade[winner] = grade[winner] + K * (1 - W_w)
            grade[loser] = grade[loser] + K * (0 - W_l)
            if grade[winner] > 9999: grade[winner] = 9999
            if grade[loser] < 0: grade[loser] = 0

            # 점수조정 배열에 추가
            md_grade.append({"id": winner, "grade": grade[winner]})
            md_grade.append({"id": loser, "grade": grade[loser]})

        # 점수 조정
        api.change_grade(BASE_URL, headers, md_grade)

        # 정보 불러오기(대기열, 유저 등급)
        waiting = api.waiting_line(BASE_URL, headers)
        # userinfo = api.user_info(BASE_URL, headers)

        # 정렬 후 등급이 비슷한 유저끼리 매칭(대기열이 홀수인경우 중간유저 남김)
        match_user = []
        for user in waiting["waiting_line"]:
            # 등급 조회 및 대상자 목록에 추가
            match_user.append([grade[user["id"]], user["id"]])

        match_user.sort()
        
        pairs = []
        lth = len(match_user)

        # 홀수라면(가운데 제외)
        if lth % 2:
            tmp = []
            for i in range(lth):
                if i == lth // 2: continue
                if len(tmp) < 2: tmp.append(match_user[i][1])
                if len(tmp) == 2:
                    pairs.append(tmp)
                    tmp = []
        # 짝수라면 모두 포함
        else:
            tmp = []
            for i in range(lth):
                if len(tmp) < 2: tmp.append(match_user[i][1])
                if len(tmp) == 2:
                    pairs.append(tmp)
                    tmp = []
        # 매치 요청 보내기
        print('매칭대상목록', pairs)
        api.match(BASE_URL, headers, pairs)
        
    api.get_score(BASE_URL, headers)


# 메인 함수 실행
if __name__ == '__main__':
    # 메인 프로그램으로서 실행 ...
    main()