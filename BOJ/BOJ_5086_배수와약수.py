# BOJ 5086 배수와 약수

while True:
    a, b = map(int, input().split())
    if not a and not b: break
    if b // a and not b % a: print('factor')
    elif a // b and not a % b: print('multiple')
    else: print('neither')