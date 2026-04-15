lidl = {
     "Jedzenie": {
        "owoce": 40,
        "mięsko": 30,
        "warzywka" : 20
    },
    "Picie": {
        "oranżada helena": 20,
        "pepsi": 30,
        "sok Kubuś" : 15
    }
}

while(True):
    print("> Lidlek")
    print("> Wybierz opcje")
    print("1) Dodaj produkt")
    print("2) Usuń produkt")
    print("3) Sprawdź dostępność produktu")
    print("4) Wyświetl wszystkie produkty")
    print("X) Wyjdź")
    Wesker = input("Opcja nr : ")
    if Wesker == '1':
        kot = input("Do czego dodać: ")
        key = input("Co chcesz jako produkt: ")
        value = int(input("Podaj ilość produktów: "))
        lidl[kot][key] = value
        print(lidl)
        break
    elif Wesker == '2':
        kot2 = input("Z czego chcesz usunąć: ")
        key2 = input("Co chcesz usunąć: ")
        del lidl[kot2][key2]
        print(lidl)
        break
    elif Wesker == '3':
        kot3 = input("Czego dostępność chcesz zobaczyć: ")
        key3 = input("Wprowadź co wyświetlić: ")
        print(lidl[kot3][key3])
        break
    elif Wesker == '4':
        kot4 = input("Jaką kategorie chcesz zobaczyć?: ")
        lidl[kot4]
        print(lidl)
        break
    elif Wesker == "X":
        break

        