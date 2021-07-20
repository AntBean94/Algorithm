# SWEA 3316 동아리실 관리하기

def check(a, b):
    for i in a:
        for j in b:
            if i==j:
                return True
    return False


N = int(input())
for _ in range(N):
    schdule = input()

    info = [0] * 16
    cases = ['A', 'B', 'C', 'D', 'AB', 'AC', 
            'AD', 'BC', 'BD', 'CD', 'ABC', 
            'ABD', 'ACD', 'BCD', 'ABCD']

    owner = [[0, 4, 5, 6, 10, 11, 12, 14],
            [1, 4, 7, 8, 10, 11, 13, 14],
            [2, 5, 7, 9, 10, 12, 13, 14],
            [3, 6, 8, 9, 11, 12, 13, 14]]

    for s in schdule:
        if s=='A':
            for i in owner[0]:
                c = cases[i]
                for j in range(15):
                    d = cases[j]
                    if check(c, d):
                        info[j] += info[]
        