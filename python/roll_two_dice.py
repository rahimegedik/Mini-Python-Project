from random import*

dn = int(input("Desired sum: "))

while sum != dn:
    first= randint(1,6)
    second = randint(1,6)
    sum = first + second

    print(str(first)+" and "+str(second)+" = "+str(sum))

