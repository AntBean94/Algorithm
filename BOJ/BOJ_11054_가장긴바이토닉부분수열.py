# BOJ 11054 가장 긴 바이토닉 부분 수열

'''
앞, 뒤로 LIS를 구한다.
앞에서 시행한 결과값과 뒤에서 시행한 결과값을 인덱스에 저장
각 인덱스를 합치고
최댓값에 -1이 정답
'''

N = int(input())
arr = list(map(int, input().split()))
# 앞 => 뒤
lth_a = [0] * N
table_a = [0] * 1001
for i in range(N):
    for j in range(arr[i]):
        if table_a[j] + 1 > table_a[arr[i]]:
            table_a[arr[i]] = table_a[j] + 1
        lth_a[i] = table_a[arr[i]]

# 뒤 => 앞
lth_b = [0] * N
table_b = [0] * 1001
for i in range(N-1, -1, -1):
    for j in range(arr[i]):
        if table_b[j] + 1 > table_b[arr[i]]:
            table_b[arr[i]] = table_b[j] + 1
        lth_b[i] = table_b[arr[i]]

for i in range(N):
    lth_a[i] += lth_b[i]

print(max(lth_a) - 1) 