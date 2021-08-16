# BOJ 2920 음계

arr = list(map(int, input().split()))
start = arr[0]
ans = ""
if start==1:
    ans = "ascending"
    for i in range(1, 9):
        if i != arr[i-1]:
            ans = "mixed"
            break
elif start==8:
    ans = "descending"
    for i in range(8, 0, -1):
        if (9 - i) != arr[i-1]:
            ans = "mixed"
            break
else:
    ans = "mixed"
print(ans)
