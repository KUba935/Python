import string
import random

 # def funkcja():
    # """
    # opis funkcji
    # """
    # imie = "imie"
   # wiek = 15
   # print(F"Witaj {imie}, masz {wiek} lat")
   # print(string.digits)
   # print(string.ascii_uppercase)
   # print(string.ascii_letters)
   # x = random.choice([2, 0, 1, 1, 230.5])
   # print(F"Losowy numer {x}")
    
# funkcja()

def numer_rejestracyjny():
    """
    Generuje losowy numer rejestracyjny
    """
    numery = string.digits
    litery = string.ascii_uppercase
    losowo = random.choice([numery,litery])


    lista = ["LU"]

    for _ in range(5):
        lista.append(losowo)

