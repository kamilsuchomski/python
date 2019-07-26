from decimal import *

def decimal_list():

    def myrange(start, stop, step):
        while start <= stop:
            yield start
            start += step
    
    dec_list = []

    for i in myrange(2.5, 5.5, 0.5):
        dec = Decimal(i)
        dec_list.append(dec)

    return dec_list
