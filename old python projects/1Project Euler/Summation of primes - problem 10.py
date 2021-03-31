
def composite(num):
    for i in range(2, num):
        value = 'True'
        if num % i == 0:
            value = 'composite'
        else:
            value = 'prime'
        return print(value)

while True:
    composite(int(input('enter number: ')))