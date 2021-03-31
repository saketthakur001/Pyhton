import time
composite = []
prime = [2]
num = 2

while len(prime) <= 1001:
    for i in range(2, num):
        if num % i == 0:
            composite.append(num)
            break
    for i in range(2, num):
        if num not in composite:
            prime.append(num)
            break
    num += 1
print(prime[-2])
