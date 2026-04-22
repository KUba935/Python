rowery = {
    "rower1": {
        "id": 1,
        "model": "Wesker",
        "typ": "Miejski",
        "Cena_za_godzine": 100,
        "Dostępny": True
    },

    "rower2": {
        "id": 2,
        "model": "Ryszard",
        "typ": "Szosowy",
        "Cena_za_godzine": 200,
        "Dostępny": True
    },

    "rower3": {
        "id": 3,
        "model": "Cross",
        "typ": "Górski",
        "Cena_za_godzine": 300,
        "Dostępny": False
    }

}

def wypozycz():
	oop = input("jaki rower wypozyczasz")
	dostep = rowery[oop]["dostepny"]
	if dostep == True:
		rowery[oop]["dostepny"] == False
		print(F"pomyslnie {oop}")
	else:
		print(F"rowe {oop} nie istnieje")
            
def	oddaj():
	oddaj = input("jaki rower chcesz oddać?: ")
	dostep = rowery[oddaj]["dostepny"]
	if dostep == False:
		print("oddales")

while(True):
    print("> Rowerki")
    print("> Wybierz opcję")
    print("1) Wyświetl wszystkie rowery")
    print("2) Wyświetl dostępne rowery")
    print("3) Wypożycz rower")
    print("4) Oddaj rower")
    print("5) Koszt wypożyczenia")
    print("6) Najtańszy i najdroższy rower")
    print("X) Wyjdź") 
    Reigns = input("Opcja nr : ")
    if Reigns == '1':
        rowery
        print(rowery)
    if Reigns == '2':
        rowery
        print(rowery)
    elif Reigns == '3':
        wypozycz()
    elif Reigns == '4':
        oddaj()


 