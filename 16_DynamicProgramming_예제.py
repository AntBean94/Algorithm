# 16강 다이나믹 프로그래밍 (Dynamic Programming) 예제

# fibonacci 수열 (상향식)
def Fibo_dp_up(n):
    arr = [0] * n
    for i in range(0, n):
        if i < 2:
            arr[i] = 1
        else:
            arr[i] = arr[i-1] + arr[i-2]
    return arr[n-1]

# 재귀
def Fibo_recur(n):
    if n == 1: return 1
    if n == 2: return 1
    return Fibo_recur(n-1) + Fibo_recur(n-2)

# 재귀 => dp (memoization)
arr = [0] * 100
def Fibo_dp(n):
    if n == 1: return 1
    if n == 2: return 1
    if arr[n] != 0:
        return arr[n]
    return Fibo_dp(n - 1) + Fibo_dp(n - 2)    


print(Fibo_dp_up(int(input())))    