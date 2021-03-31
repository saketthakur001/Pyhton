dig3 = [num for num in range(100, 999+1)]
dig3.reverse()
palindrom = []

for first in dig3:
    for sec in dig3:
        product = str(first * sec)
        if product[0:3] == product[-1]+product[-2]+ product[3]:
            palindrom.append(product)
num = 0
while True:
    for i in palindrom:
        if int(i)>int(num):
            num = i
    break
print(num)