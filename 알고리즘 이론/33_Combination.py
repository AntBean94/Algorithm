# 33 조합(Combination)

N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
result = []

def combination(arr, m):
    tmp = []
    start = 0

    def generate(i):
        if len(tmp) == m: 
            result.append(list(tmp))
        else:
            for j in range(i, len(arr)):
                tmp.append(arr[j])
                generate(j + 1)
                tmp.pop()

    generate(start)

combination(arr, M)

print(result)