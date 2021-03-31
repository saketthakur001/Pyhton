#https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python
def make_negative( number ):
    if  number > 0:
        print(number * -1)
        return number * (-1)
    else:
        print(number)
        return number

make_negative(-34)