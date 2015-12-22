from math import e
from decimal import *
#show-e-to-n-digit
while True:
    try:
        useri = int(input("how many digits of e do you want to see? (Max 53):"))
        break
    except ValueError:
        print("you gone goofed, provide an integer")


# useri amount of decimal
getcontext().prec = useri
a = Decimal(e) + Decimal(0)
print(a)
print(len(str(a)))

input("type anything")