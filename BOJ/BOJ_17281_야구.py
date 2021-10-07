# BOJ 17281 ⚾

'''
50이닝
1번: 4번 타자
8명의 선수로 순서를 정하는 경우의 수
= 5,040 가지

40,320 * 50(이닝) * 27 = 약 5000만

점수이동 처리
=> 배열 이동(X), 최종 주자만 확인(O)
결과: 통과
'''

from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
result = [list(map(int, input().split())) for _ in range(N)]
ans = 0

arr = [i for i in range(2, 10)]
for case in permutations(arr, 8):
    score = 0
    seq = case[:3] + (1,) + case[3:]
    # 현재 타순
    t = 0
    # 이닝
    for i in range(N):
        out_cnt = 0
        Q = []
        tmp = 0
        while out_cnt < 3:
            now = seq[t]
            rst = result[i][now-1]
            if not rst: out_cnt += 1
            else:
                Q.append(rst)
                tmp += 1
            t = (t + 1) % 9
        # 점수 계산
        sm = 0
        for j in range(tmp-1, -1, -1):
            sm += Q[j]
            if sm > 3:
                score += (j + 1)
                break

    # 결과 확인
    if score > ans: ans = score
print(ans)