# BOJ 11758 CCW

'''
CCW(Counter Clock Wise) 알고리즘

A = (x1, y1, 0), B = (x2, y2, 0), C = (x3, y3, 0)

a(vector) = AB(vector) = (x2 - x1, y2 - y1, 0)
b(vector) = AC(vector) = (x3 - x1, y3 - y1, 0)

a(vector) X b(vector) = (0, 0, (x2 - x1)(y3 - y1) - (x3 - x1)(y2 - y1))

D = (x2 - x1)(y3 - y1) - (x3 - x1)(y2 - y1)
case 1. D = 0
- 일직선
case 2. D < 0
- 시계 방향
case 3. D > 0
- 반시계 방향
'''

class Vector():
    def __init__(self, x = "0", y = "0", z = "0"):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

input_val = [list(map(int, input().split())) for _ in range(3)]

A = Vector(input_val[0][0], input_val[0][1])
B = Vector(input_val[1][0], input_val[1][1])
C = Vector(input_val[2][0], input_val[2][1])

def ccw(a, b, c):
    D = (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)
    return D

result = ccw(A, B, C)
if result == 0: print(0)
elif result > 0: print(1)
else: print(-1)