# Programmers 카카오 T 바이크 관리 시뮬레이션

'''
카카오 코딩테스트 2차 기출문제(2021년도 하반기 공채)
'''


import requests
import json

BASE_URL = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"

with open('./secrets.json', 'r') as f:
    json_data = json.load(f)
    print(type(json_data))
    # json_data = json.dumps(json_data)

print(json_data['X_Auth_Token'], type(json_data))
# start api
headers = {
    'X-Auth-Token': json_data['X_Auth_Token'],
    'Content-Type': 'application/json'
}
payload = {'problem': 1}
res = requests.post(f'{BASE_URL}/start', headers=headers, params=payload)
print(res.text, type(res.text))
print(res.text["auth_key"])