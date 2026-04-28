def funkcja(a: int, b: int, c: int):
    x = a + b + c 
    final = x / 3.14
    return final

print(funkcja(2, 2, 2))

def pies():
    pies = 1 + 2
    pies2 = 3 + 3

    return pies, pies2

def kot1(a, b):
    q = a + b
    return q

def kot2(a, b):

    final = kot1(a,b)

    d = final - a - b
    return d

print(kot2(3, 4))

def zakres(a, b):
    for x in range(a, b):
        if x % 21 == 0:
            print("cos")

zakres(1, 5)

def funkcja2():
    for z in range(1, 1024):
        if z % 21 == 0:
            print("john")
        if z % 37 == 0:
            print("paul")

funkcja2()

def funkcja3(x: int):
    if x == 1:
        print("?:-)")
    if x == 2:
        print(":-|")
    if x == 3:
        print(":-(")
    else:
        pass

funkcja3(1)