
while True:
    try:
        comp = []
        num = int(input("enter a number: "))
        for i in range(2, num):
            if num % i == 0:
                comp.append(i)
        print(num, " is divisible by ", comp)
    except ValueError:
        print('try something meaningful ¯\_(ツ)_/¯')