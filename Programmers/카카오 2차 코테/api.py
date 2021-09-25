# 2022 카카오 블라인드채용 - 2차 코딩테스트

import requests
import json


# Start API
# 문제를 풀기 위한 key를 발급한다. Start API를 실행하면 파라미터로 전달한 문제 번호에 맞게 각 자전거 대여소 및 트럭에 대한 정보를 초기화한다.
def start(url, headers, problem):
    payload = {'problem': problem}
    res = requests.post(f'{url}/start', headers=headers, params=payload)
    print('시작 응답:', res.status_code)
    print('시작 데이터:', res.json())
    return res.json()


# Waiting Line API
# 현재 대기열에서 매칭을 대기 중인 유저들의 정보를 반환한다.
def waiting_line(url, headers):
    res = requests.get(f'{url}/waiting_line', headers=headers)
    print('대기열 응답:', res.status_code)
    print('대기열 데이터:', res.json())
    return res.json()


# Game Result API
# 이번 턴에 게임이 끝난 유저들의 게임 결과를 반환한다.
def game_result(url, headers):
    res = requests.get(f'{url}/game_result', headers=headers)
    print('게임 결과 응답:', res.status_code)
    print('게임 결과 데이터:', res.json())
    return res.json()


# User Info API
# 모든 유저들의 현재 등급을 반환한다.
def user_info(url, headers):
    res = requests.get(f'{url}/user_info', headers=headers)
    print('현재 등급 응답:', res.status_code)
    print('현재 등급 데이터:', res.json())
    return res.json()


# Mathch API
# 대기열에서 매칭 대기 중인 두 유저를 매칭하여 게임을 시작하도록 한다. 매칭할 유저의 쌍을 배열에 담아 서버에 전달하면 서버에서는 다음과 같은 일이 진행된다.
'''
1. 매칭된 두 유저의 아이디를 확인하여 대기열에서 삭제, 비정상 데이터는 무시
2. 서버 내부 데이터를 반영해 승패여부와 게임 시간(t)를 결정
3. 매칭 요청이 성공하면 게임 서버의 상태가 ready로 변경되며 시간이 1분 진행된다.
'''
def match(url, headers, pairs):
    data = {
        "pairs": pairs
    }
    data = json.dumps(data)
    res = requests.put(f'{url}/match', headers=headers, data=data)
    print('매치 응답:', res.status_code)
    print('매치 결과', res.json())
    return res.json()


# Change Grade API
# 여러 유저의 등급을 수정할 수 있다. 등급의 범위는 0이상 9,999 이하 정수이다. 서버에 저장된 등급은 매칭에 영향을 주지 않는다.
def change_grade(url, headers, commands):
    data = {
        'commands': commands
    }
    data = json.dumps(data)
    res = requests.put(f'{url}/change_grade', headers=headers, data=data)
    print('등급 수정 응답:', res.status_code)
    print('등급 수정 결과:', res.json())
    return res.json()


# Score API
# 시뮬레이션이 끝난 뒤 정확성 점수와 효율성 점수, 총점을 반환한다.
def get_score(url, headers):
    res = requests.get(f'{url}/score', headers=headers)
    print(res.status_code)
    print(res.json())
    return res.json()