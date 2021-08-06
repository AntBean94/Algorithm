# BOJ 14891 톱니바퀴

'''
톱니바퀴는 4개
바퀴 살은 8개
[01234567]
0이 12시
2 => 오른쪽 접점
6 => 왼쪽 접점

python list를 큐로 활용
시계방향: 7을 빼서 0에 삽입
반시계방향: 0을 빼서 7에 삽입

회전 방향 체크
1. 번호와 회전방향 입력
2. 리스트에 회전 톱니바퀴 정보 담는다.
3. 회전 톱니바퀴만 회전
4. 방향은 1과 3이 정방향 2, 4가 정방향

점수 출력은 [2**바퀴번호(0 ~ 3)] 
'''

import sys
input = sys.stdin.readline

# 톱니바퀴 정보
gears = [input().rstrip() for _ in range(4)]

# 회전 정보
K = int(input())
cycle_info = [list(map(int, input().split())) for _ in range(K)]

for n, d in cycle_info:
    # 리스트에 회전 톱니바퀴 정보 담기
    cyc = [n]
    dir = [d]
    p = n
    # 정방향
    while p < 4:
        if gears[p-1][2] != gears[p][6]:
            cyc.append(p+1)
            if (n + p + 1) % 2:
                dir.append(-d)
            else:
                dir.append(d)
            p += 1
        else:
            break
    p = n - 1
    # 역방향
    while p > 0:
        if gears[p-1][2] != gears[p][6]:
            cyc.append(p)
            if (n + p) % 2:
                dir.append(-d)
            else:
                dir.append(d)
            p -= 1
        else:
            break

    # print(cyc, dir)
    # 톱니바퀴 회전
    for i in range(len(cyc)):
        a = cyc.pop(0) - 1
        b = dir.pop(0)
        # 정방향
        if b == 1:
            gears[a] = gears[a][7] + gears[a][:7]
        # 역방향
        else:
            gears[a] = gears[a][1:] + gears[a][0]
    # print(gears)

# 점수계산
point = 0
for i in range(4):
    if gears[i][0] == '1':
        point += 2 ** i
print(point)
