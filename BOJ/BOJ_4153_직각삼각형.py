# BOJ 4153 직각삼각형

T = True
while T:
    arr = list(map(int, input().split()))
    T = sum(arr)
    if not T:
        break
    arr = sorted(arr)
    if arr[0]**2 + arr[1]**2 == arr[2]**2:
        print('right')
    else:
        print('wrong')

    
    