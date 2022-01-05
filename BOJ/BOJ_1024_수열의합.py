# BOJ 1024 수열의 합

'''
1. 수열이 존재하면 첫 줄에 공백으로 구분하여 수열 출력
2. 수열의 길이가 100보다 크거나 없으면 -1 출력

등차수열의 합
길이를 기준으로 L부터 100까지 확인

길이가 L이고 차가 1인 등차수열의 합(N)
N = (2a + L-1)L / 2

길이랑 합이 주어졌을 때 정수해(시작값)가 존재하는지 확인
a에 관한 식으로 정리
a = (2N/L - L + 1) / 2
'''

N, L = map(int, input().split())
arr = []

# 길이가 L인 수열부터 확인
for l in range(L, 101):
    a = (2 * N / l - l + 1) / 2
    if a % 1 == 0 and a > -1:
        a = int(a)
        arr = [i for i in range(a, a + l)]
        break
if arr: print(*arr)
else: print(-1)