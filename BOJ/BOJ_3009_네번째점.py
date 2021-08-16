# BOJ 3009 네 번째 점

a = []
b = []
for i in range(3):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
if a[0] == a[1]:
    a = a[2]
elif a[0] == a[2]:
    a = a[1]
else:
    a = a[0]
if b[0] == b[1]:
    b = b[2]
elif b[0] == b[2]:
    b = b[1]
else:
    b = b[0]
print(a, b)

    
