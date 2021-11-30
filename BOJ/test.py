a = [1, 2, 3, 4, 5]
b = []
for i in a:
    b.append(i)
a = b
b[2] = 100
print(a, b)