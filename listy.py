# Listy
lista = [2, 'pies', 6, 7]
print(lista[0])
print(lista[-1])
lista.append("pieseczek")
print(lista)
del lista[2]
print(lista)
if 'pies' in lista:
    print("tak")
else:
    print("nie")

for _ in lista:
    print(_)

print("-" * 100)
# słowniki

slownik = {
    "Marcel": 20,
    "Jakub" : 67,
    "Sebastian" : 69,
    "Ada" : 88,
}

slownik["Mateusz"] = 85
print(slownik)

del slownik["Leon"]
print(slownik)

if "Ada" in slownik:
    print("Tak")
else:
    print("Nie")

for key, value in slownik.items():
    print(F"klucz: {key}, wartość: {value}")