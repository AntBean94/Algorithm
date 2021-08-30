# BOJ 11444 피보나치 수 6

'''
행렬의 거듭제곱
(1 1)
(1 0)
'''

def mul(arr1, arr2):
    arr = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            result = 0
            for k in range(2):
                result += arr1[i][k] * arr2[k][j]
            arr[i][j] = result % 1000000007
    return arr

def recur(arr, r):
    if r == 1:
        return arr
    # 홀수인경우
    elif bin(r)[-1] == '1':
        result = mul(arr, recur(arr, r - 1))
        return result
    else:
        result = recur(arr, r // 2)
        return mul(result, result)

N = int(input())
seed = [[1, 1], [1, 0]]
ans = recur(seed, N)
print(ans[0][1])