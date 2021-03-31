"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
divi = 0

for twenty in range(2,20):
    for num in range(99**99):
        if num % twenty == 0:
            divi += 1
            print(divi)
    print(divi)
