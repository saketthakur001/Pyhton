loop = [1, 2]
result = 0
pos = 0

for i in loop:
    if i < 4000000:
        pos = loop[-1] + loop[-2]
        loop.append(pos)
    if i % 2 == 0:
        result += i

print(result)
