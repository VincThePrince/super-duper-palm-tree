import random
n = 100000000
b = []
for i in range (0,n):
    a = random.randint(1,6)
    b.append(a)
c = sum(b)
M = c/n
print(M)
