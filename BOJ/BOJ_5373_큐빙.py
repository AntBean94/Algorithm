# BOJ 5373 큐빙

'''
모두 돌린뒤 가장 윗면의 색상을 구하는 프로그램 작성

U:윗 면, D:아랫 면
F:앞 면, B:뒷 면
L:왼쪽 면, R:오른쪽 면

+:시계 방향, -:반시계 방향

w: 흰색, y: 노란색, r: 빨간색
o: 오렌지색, g: 초록색, b: 파란색

전개도
      |U U U|
    l |U U U|
      |U U U|
L L L |F F F| R R R
L L L |F F F| R R R
L L L |F F F| R R R
      |D D D|
    l |D D D| r
      |D D D|

         u
      |B B B|
    r |B B B| l
      |B B B|
         d

자료 형태: {U: [[]], F: [[]] ...}
'''

import sys
input = sys.stdin.readline

face = {'U': 'w', 'D': 'y', 'F': 'r', 'B': 'o', 'L': 'g', 'R': 'b'}
I = {
    'F': {
        'U': [[2, 0], [2, 1], [2, 2]], 
        'R': [[0, 0], [1, 0], [2, 0]], 
        'D': [[0, 2], [0, 1], [0, 0]],
        'L': [[2, 2], [1, 2], [0, 2]]
    },
    'B': {
        'U': [[0, 2], [0, 1], [0, 0]],
        'L': [[0, 0], [1, 0], [2, 0]],
        'D': [[2, 0], [2, 1], [2, 2]],
        'R': [[2, 2], [1, 2], [0, 2]]
    },
    'U': {
        'B': [[0, 2], [0, 1], [0, 0]],
        'R': [[0, 2], [0, 1], [0, 0]],
        'F': [[0, 2], [0, 1], [0, 0]],
        'L': [[0, 2], [0, 1], [0, 0]]
    },
    'D': {
        'F': [[2, 0], [2, 1], [2, 2]],
        'R': [[2, 0], [2, 1], [2, 2]],
        'B': [[2, 0], [2, 1], [2, 2]],
        'L': [[2, 0], [2, 1], [2, 2]]
    },
    'L': {
        'U': [[0, 0], [1, 0], [2, 0]],
        'F': [[0, 0], [1, 0], [2, 0]],
        'D': [[0, 0], [1, 0], [2, 0]],
        'B': [[2, 2], [1, 2], [0, 2]]
    },
    'R': {
        'U': [[2, 2], [1, 2], [0, 2]],
        'B': [[0, 0], [1, 0], [2, 0]],
        'D': [[2, 2], [1, 2], [0, 2]],
        'F': [[2, 2], [1, 2], [0, 2]]
    }
}

T = int(input())
for tc in range(T):
    cube = {key: list([value] * 3 for _ in range(3)) for key, value in face.items()}
    N = int(input())
    cmds = list(map(str, input().split()))
    
    for cmd in cmds:
        c1 = cmd[0]
        c2 = cmd[1]
        s = list(I[c1].keys())
        # 회전(시계 방향)
        if c2 == '+':
            # 측면
            for i in range(3):
                a, b, c, d = I[c1][s[0]][i], I[c1][s[1]][i], I[c1][s[2]][i], I[c1][s[3]][i]
                cube[s[0]][a[0]][a[1]], cube[s[1]][b[0]][b[1]], cube[s[2]][c[0]][c[1]], cube[s[3]][d[0]][d[1]] = cube[s[3]][d[0]][d[1]], cube[s[0]][a[0]][a[1]], cube[s[1]][b[0]][b[1]], cube[s[2]][c[0]][c[1]]
            # 정면
            cube[c1][0][0], cube[c1][0][2], cube[c1][2][2], cube[c1][2][0] = cube[c1][2][0], cube[c1][0][0], cube[c1][0][2], cube[c1][2][2]
            cube[c1][0][1], cube[c1][1][2], cube[c1][2][1], cube[c1][1][0] = cube[c1][1][0], cube[c1][0][1], cube[c1][1][2], cube[c1][2][1]
        # 반시계 방향
        else:
            for i in range(3):
                a, b, c, d = I[c1][s[0]][i], I[c1][s[1]][i], I[c1][s[2]][i], I[c1][s[3]][i]
                cube[s[0]][a[0]][a[1]], cube[s[1]][b[0]][b[1]], cube[s[2]][c[0]][c[1]], cube[s[3]][d[0]][d[1]] = cube[s[1]][b[0]][b[1]], cube[s[2]][c[0]][c[1]], cube[s[3]][d[0]][d[1]], cube[s[0]][a[0]][a[1]]
            cube[c1][0][0], cube[c1][0][2], cube[c1][2][2], cube[c1][2][0] = cube[c1][0][2], cube[c1][2][2], cube[c1][2][0], cube[c1][0][0]
            cube[c1][0][1], cube[c1][1][2], cube[c1][2][1], cube[c1][1][0] = cube[c1][1][2], cube[c1][2][1], cube[c1][1][0], cube[c1][0][1]
    for i in range(3):
        sys.stdout.writelines("".join(cube['U'][i]) + "\n")