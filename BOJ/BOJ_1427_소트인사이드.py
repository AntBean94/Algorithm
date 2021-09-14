# BOJ 1427 소트인사이드

N_str = input()
arr = []
for i in N_str:
    arr.append(int(i))
for i in sorted(arr, reverse=True):
    print(i, end="")