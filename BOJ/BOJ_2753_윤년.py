# BOJ 2753 윤년

year = int(input())
condition1 = year % 4
condition2 = year % 100 
condition3 = year % 400
if condition1==0 and condition2!=0 or condition3==0:
    print('1')
else:
    print('0')