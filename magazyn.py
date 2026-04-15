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
    Wesker = int(input("Opcja nr : "))
    if Wesker == '1':
        slownik = input("Do której kategorii dodać: ")
        key = input("Wprowadź co dodać jako produkt: ")
        value = int(input("Wprowadź ile produktów dodać: "))
        lidl[slownik][key] = value
        print(lidl)
        break
    elif Wesker == '2':
        slownik2 = input("Z jakiej kategorii usunąć: ")
        key2 = input("Wprowadź co usunąć: ")
        del lidl[slownik2][key2]
        print(lidl)
        break
    elif Wesker == '3':
        slownik3 = input("Jaką kategorie chcesz zobaczyć?: ")
        key3 = input("Wprowadź co wyświetlić: ")
        print(lidl[slownik3][key3])
        break
    elif Wesker == '4':
        slownik4 = input("Jaką kategorie chcesz zobaczyć?: ")
        lidl[slownik4]
        print(lidl)
        break
    elif Wesker == "X":
        break

        