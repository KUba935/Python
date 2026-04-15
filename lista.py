lista = {
   "jabłka": 2,
   "woda": 6,
   "kiełba": 1,
   "mleczko": 3
}

while(True):
    print("> Lista zakupów")
    print("> Wybierz opcje")
    print("1) Dodaj produkt")
    print("2) Usuń produkt")
    print("3) Sprawdź dostępność produktu")
    print("4) Wyświetl wszystkie produkty")
    print("X) Wyjdź")
    Wesker = input("Opcja nr : ")
    if Wesker == '1':
        key = input("Co chcesz jako produkt: ")
        value = int(input("Podaj ilość produktów: "))
        lista[key] = value
        print(lista)
    elif Wesker == '2':
        key2 = input("Co chcesz usunąć: ")
        del lista[key2]
        print(lista)
    elif Wesker == '3':
        key3 = input("Wprowadź co wyświetlić: ")
        print(lista[key3])
    elif Wesker == '4':
        lista
        print(lista)
    elif Wesker == "X":
        break