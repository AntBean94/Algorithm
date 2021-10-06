# Programmers 최소직사각형

# 최댓값 갱신
def solution(sizes):
    answer = 0
    w, h = 0, 0
    for y, x in sizes:
        # y또는 x가 기존값보다 큰 경우
        ty, tx = max(w, x), max(h, y)
        ny, nx = max(w, y), max(h, x)
        if ty * tx < ny * nx:
            w, h = ty, tx
        else:
            w, h = ny, nx
        answer = w * h
    return answer