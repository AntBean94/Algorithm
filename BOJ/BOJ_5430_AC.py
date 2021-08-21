# BOJ 5430 AC

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    func = input().rstrip()
    N = int(input())
    info = input().rstrip()
    if len(info) == 2:
        arr = []
    else:
        arr = list(map(int, info[1:-1].split(',')))
    
    # 함수 실행
    s, e = 0, N
    check = True
    err = False
    for f in func:
        if f == 'R':
            check = not check
        else:
            # 비어있는데 출력하려고 하면
            if s == e:
                err = True
                break
            # 정방향
            if check:
                s += 1
            # 역방향
            else:
                e -= 1

    if err:
        print('error')
    else:
        if check:
            print('[' + ','.join(map(str, arr[s:e])) + ']')
        else:
            print('[' + ','.join(map(str, arr[s:e][::-1])) + ']')