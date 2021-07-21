# SWEA 3316 동아리실 관리하기

def check(a, b):
    for i in a:
        for j in b:
            if i==j:
                return True
    return False


N = int(input())
for tc in range(1, N+1):
    schdule = input()

    info = [0] * 16
    info2 = [0] * 16
    cases = ['A', 'B', 'C', 'D', 'AB', 'AC', 
            'AD', 'BC', 'BD', 'CD', 'ABC', 
            'ABD', 'ACD', 'BCD', 'ABCD']

    owner = [[0, 4, 5, 6, 10, 11, 12, 14],
            [1, 4, 7, 8, 10, 11, 13, 14],
            [2, 5, 7, 9, 10, 12, 13, 14],
            [3, 6, 8, 9, 11, 12, 13, 14]]

    manager = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    # 초기값 설정(A 소유, 첫번째 관리자)
    f = schdule[0]
    if 'A'==f:
        data = [0, 4, 5, 6, 10, 11, 12, 14]
        for i in data:
            info[i] = 1
    else:
        if f=='B':
            data = [4, 10, 11, 14]
            for i in data:
                info[i] = 1
        elif f=='C':
            data = [5, 10, 12, 14]
            for i in data:
                info[i] = 1
        else:
            data = [6, 11, 12, 14]
            for i in data:
                info[i] = 1
    # 경우의 수 계산
    for s in range(1, len(schdule)):
        num = manager[schdule[s]]
        pre_num = manager[schdule[s-1]]
        for i in owner[num]:
            c = cases[i]
            pre_num = manager[schdule[s-1]]
            for j in owner[pre_num]:
                d = cases[j]
                if check(c, d):
                    info2[i] += info[j]
        info = info2
        info2 = [0] * 16
        
    print('#{} {}'.format(tc, sum(info)%1000000007))