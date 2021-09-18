# BOJ 17140 이차원 배열과 연산

'''
정렬 순

1. 등장횟수 오름차순
2. 크기 오름차순

{3: 1, 1: 2}
value값에 맞춰 정렬

정렬한 다음 하나씩 넣기
최대길이에 맞춰서 0을 추가

R, C길이에 따라 연산 체인지

100개넘으면 버린다.
'''

R, C, K = map(int, input().split())
arr = [[0] * 100 for _ in range(100)]
for i in range(3):
    row = list(map(int, input().split()))
    for j in range(3):
        arr[i][j] = row[j]

t = 0
check = True
while t <= 100:
    r, c = 0, 0
    # 검증
    if arr[R-1][C-1] == K:
        print(t)
        break
    elif t == 100:
        print(-1)
    
    # 정렬
    b_cnt = 0
    for i in range(100):
        pot = {}
        a_cnt = 0
        for j in range(100):
            # 행정렬
            if check:
                num = arr[i][j]
                if num == 0: continue
                if num in pot:
                    pot[num] += 1
                else:
                    pot[num] = 1
            # 열정렬
            else:
                num = arr[j][i]
                if num == 0: continue
                if num in pot:
                    pot[num] += 1
                else:
                    pot[num] = 1
            
        # 정렬된 값 넣기
        if not pot: continue
        pot = sorted(pot.items(), key=lambda x: (x[1], x[0]))
        idx = 0
        for key, value in pot:
            if check:
                arr[i][idx] = key
                arr[i][idx + 1] = value
            else:
                arr[idx][i] = key
                arr[idx + 1][i] = value
            idx += 2
            if idx == 100: break
        
        if check:
            if idx > c: c = idx
        else:
            if idx > r: r = idx
        
        # 이외의값은 0으로 바꾸기
        while idx < 100:
            if check:
                if arr[i][idx]: arr[i][idx] = 0
            else:
                if arr[idx][i]: arr[idx][i] = 0
            idx += 1
                
        b_cnt += 1

    if check:
        if b_cnt > r: r = b_cnt
    else:
        if b_cnt > c: c = b_cnt
    
    # 방향 설정
    if r >= c: check = True
    else: check = False
    t += 1