# Programmers 카카오 T 바이크 관리 시뮬레이션

'''
카카오 코딩테스트 2차 기출문제(2021년도 하반기 공채)
'''

import requests
import json


# auth token 불러오기
with open('./secrets.json', 'r') as f:
    token_data = json.load(f)
    print(type(token_data))
    # json_data = json.dumps(json_data)
print(token_data['X-Auth-Token'], type(token_data))


# API URL
BASE_URL = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
content_type = 'application/json'
headers = {
    'X-Auth-Token': token_data['X-Auth-Token'],
    'Content-Type': content_type
}
problem = 1


# Start API
# 문제를 풀기 위한 key를 발급한다. Start API를 실행하면 파라미터로 전달한 문제 번호에 맞게 각 자전거 대여소 및 트럭에 대한 정보를 초기화한다.
def start(url, headers, problem):
    payload = {'problem': problem}
    res = requests.post(f'{url}/start', headers=headers, params=payload)
    print('시작응답:', res.status_code)
    print('시작데이터:', res.json())
    return res
res = start(BASE_URL, headers, problem)
res = res.json()
# auth key 저장
# del headers['X-Auth-Token']
headers['Authorization'] = res['auth_key']
# print(AUTH_KEY)


# Locations API
# 현재 카카오 T 바이크 서비스 시각에 각 자전거 대여소가 보유한 자전거 수를 반환한다.
def get_locations(url, headers):
    res = requests.get(f'{url}/locations', headers=headers)
    print('위치응답:', res.status_code)
    print('위치데이터:', res.json())
    return res
# res = get_locations(BASE_URL, headers)
# res = res.json()


# Trucks API
# 현재 카카오 T 바이크 서비스 시각에 각 트럭의 위치와 싣고 있는 자전거 수를 반환한다.
def get_trucks(url, headers):
    res = requests.get(f'{url}/trucks', headers=headers)
    print('트럭응답:', res.status_code)
    print('트럭데이터(위치, 자전거 보유대수):', res.json())
    return res
# res = get_trucks(BASE_URL, headers)
# res = res.json()


# Simulate API
# 현재 시각 ~ 현재 시각 + 1분 까지 각 트럭이 행할 명령을 담아 서버에 전달한다.
def simulate(url, headers, commands):
    data = {
        "commands": commands
    }
    data = json.dumps(data)
    res = requests.put(f'{url}/simulate', headers=headers, data=data)
    print(res.status_code)
    print(res.json())
    return res
# commands = [
#     {"truck_id": 0, "command": [2, 5, 4, 1, 6]},
#     {"truck_id": 1, "command": [2, 5, 4, 1, 6]}
# ]
# commands_json = json.dumps(commands)
# res = simulate(BASE_URL, headers, commands)
# res = res.json()


# Score API
# 해당 Auth key로 획득한 점수를 반환한다. 점수는 높을수록 좋다. 카카오 T 바이크 서버의 상태가 finished가 아닐 때 본 API를 호출하면 response의 score는 무조건 0.0이다.
def get_score(url, headers):
    res = requests.get(f'{url}/score', headers=headers)
    print(res.status_code)
    print(res.json())
    return res
# res = get_score(BASE_URL, headers)


# ============================ 메인 알고리즘 ============================== #
def main():
    # 0. 전략
    '''
    1) 과거 대여 요청 기록 분석
      - 과거 대여 요청 기록을 분석하여 시간대별로 각 대여소의 평균 요청수를 계산한다.
    2) 대여소 우선순위 선정
      - 대여소별로 평균 대여 요청수와 현재 자전거 보유 대수가 가장 많이 차이나는 5군데의 장소(*최적화 필요)를 내림차순으로 선정한다.
    3) 트럭 커맨드 설정
      - 각 대여소와 기타 정보(보유자전거, 거리, 자전거가 남는 대여소)를 참고하여 가장 코스트가 적은 트럭을 이용하여 자전거를 이동시킨다.
      - 트럭위치를 초기화시킨다.(사용하지 않은 트럭(또는 코스트가 남은 트럭)을 요청트래픽이 몰리는곳으로 사전에 이동, 다음날 평균 트래픽을 분석)
    
    '''

    # 1. 과거 대여 요청 기록 분석(시나리오 2에서 의미있음)
    '''
    1) 시나리오 다운로드 (1, 2, 3)
    2) 다음 시간(현재 시간 + 1분)의 평균 요청횟수와 반납횟수 => 이번 시간의 트럭 움직임에 활용(simulate 함수 마지막 절차로 트럭을 움직이므로)
    '''
    res1 = requests.get('https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem2_day-1.json')
    res2 = requests.get('https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem2_day-2.json')
    res3 = requests.get('https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem2_day-3.json')
    # print(res1.json())
    res1 = res1.json()
    res2 = res2.json()
    res3 = res3.json()
    # print(res1.keys(), type(res1.keys()))
    board = [0] * 3600
    for i in range(720):
        i = str(i)
        if i in res1.keys():
            for start, end, time in res1[i]:
                board[start] += 1
        if i in res2.keys():
            for start, end, time in res2[i]:
                board[start] += 1
        if i in res3.keys():
            for start, end, time in res3[i]:
                board[start] += 1
    # print(board[:25])
    # print(sorted(board)[::-1][:10])
    
        

    # 2. 대여소 우선순위 선정
    '''
    1) 과거 기록(시나리오)에서 다음 시간대의 평균 요청, 반납 횟수 추출
    2) 현재 시간대의 대여소별 자전거정보에 현재시간대의 평균 요청, 반납 횟수를 반영
    3) 2의 대여소별 자전거 정보에 1을 반영해 값(평균 요청횟수 - 예상 보유대수)을 산정 후 내림차순 정렬

    '''

    # 3. 트럭 커맨드 설정
    '''
    1) 우선순위가 높은 대여소 순으로 다음을 계산
    - 우선순위가 가장 낮은 대여소 위치(기본: 내림차순 정렬 기준, 최적화: 거리까지 고려), 해당위치와 가장 가까운 트럭을 결정
    - 트럭: 대여소 방문(우선순위 하), 자전거 픽업, 대여소 방문(우선순위 상), 자전거 하차, 지역 거점 이동
    - 단, 이동조건을 먼저 계산하고 남은 시간만큼만 자전거를 픽업할 수 있다.
    
    '''

# 메인 함수 실행
main()