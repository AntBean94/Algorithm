# BOJ 1912 연속합

'''
연속합

누적 값에서 -값을 추가했을때 더 작아지면 아예 초기화
그래도 더 크면 누적

2 3 -1 3 7 3 9 14 9 10
'''

N = int(input())
arr = list(map(int, input().split()))
table = [0] * (N + 1)

for i in range(N):
    if table[i] > 0:
        table[i + 1] = table[i] + arr[i]
    else:
        table[i + 1] = arr[i]
print(max(table[1:]))