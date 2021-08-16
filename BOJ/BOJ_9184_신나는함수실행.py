# BOJ 9184 신나는 함수 실행

# dp 바텀업, 탑다운
# 바텀업 => 점화식
# 탑다운

box = [[[0] * 51 for _ in range(51) ] for _ in range(51)]
for i in range(51):
    for j in range(51):
        for k in range(51):
            if i * j * k == 0:
                box[i][j][k] = 1

def W(a, b, c):
    if box[a][b][c]:
        return box[a][b][c]
    if a > 20 or b > 20 or c > 20:
        box[a][b][c] = W(20, 20, 20)
    elif a < b < c:
        box[a][b][c] = W(a, b, c-1) + W(a, b-1, c-1) - W(a, b-1, c)
    else:
        box[a][b][c] = W(a-1, b, c) + W(a-1, b-1, c) + W(a-1, b, c-1) - W(a-1, b-1, c-1)
    return box[a][b][c]

T = True
while T:
    a, b, c = map(int, input().split())
    if [a, b, c]==[-1, -1, -1]:
        break
    if a <= 0 or b <= 0 or c <= 0:
        print(f'w({a}, {b}, {c}) = 1')
    else:
        W(a, b, c)
        print(f'w({a}, {b}, {c}) = {box[a][b][c]}')
    
