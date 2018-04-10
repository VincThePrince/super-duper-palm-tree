import random
import sys
n = int(sys.argv[1])
b = []
for i in range (0,n):
    a = random.randint(1,6)
    b.append(a)
c = sum(b)
M = c/n
print(M)

print("Stef stinkt")
