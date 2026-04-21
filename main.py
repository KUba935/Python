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
    
    

    



    
    