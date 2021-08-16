# BOJ 2884 알람 시계

Hour, Minute = map(int, input().split())
Minute -= 45
if Minute < 0:
    Minute += 60
    Hour -= 1
    if Hour < 0:
        Hour = 23
print(f'{Hour} {Minute}')