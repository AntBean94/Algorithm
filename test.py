import sys
import itertools

a = 0
char = ""
for i in itertools.combinations([i for i in range(20)], 10):
    char += " ".join(map(str, i))
    char += "\n"
    a += 1
sys.stdout.write(char)
print(a)