import math
a = 600851475143
b = int (math.sqrt(a))
c = []

for i in range (3, b, 2):
    if a % i == 0:
        
        d = a // i
        c.append(i)
        c.append(d)
c.sort()
u = c
h = []

for j in c:
    for t in u:
        if j != t and j % t == 0:
            h.append(j)
            
            
            

s1 = set(c)
s2 = set(h)

final = s1 - s2

print (max(final))
