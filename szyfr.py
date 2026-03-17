import string

tekst = "KING"
klucz = int(5)

ostateczne = ''
print(tekst)

def szyfr_cezara(tekst, klucz, ostateczne):
    ostateczne=""
    for _ in tekst:
        print(_)
        numer = ord(_)
        dodanie = numer + klucz
        zaszyfrowany = chr(dodanie)
        ostateczne += zaszyfrowany
    return(ostateczne)
print(szyfr_cezara(tekst, klucz))


pieseczek = szyfr_cezara(tekst, ostateczne)

def odszyfr_cezara(tekst, klucz):
    ostateczne=""
    for _ in tekst:
        numer = ord(_)
        odejmowanie = numer - klucz
        zaszyfrowany = chr(odejmowanie)
        ostateczne += zaszyfrowany
    return(ostateczne)

pieseczek = (szyfr_cezara(tekst, klucz))

print(odszyfr_cezara(pieseczek, klucz))
        