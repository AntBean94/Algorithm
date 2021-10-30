# BOJ 2166 다각형의 면적

'''
다각형 면적 구하기
정사분면에서 0,0을 기준으로 넓이를 구한다.
좌표는 다각형을 이루는 순서대로 주어진다.
'''

import sys
input = sys.stdin.readline

N = int(input())
coor = [list(map(int, input().split())) for _ in range(N)]
coor.append(coor[0])
xy, yx = 0, 0
for i in range(N):
    xy += coor[i][0] * coor[i+1][1]
    yx += coor[i][1] * coor[i+1][0]
print(round(abs(xy - yx) / 2, 1))