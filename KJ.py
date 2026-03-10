import string

tekst = "KING"
klucz = int(5)


def szyfr_cezara(tekst, klucz):
    ostateczne=""
    for _ in tekst:
        print(_)
        numer = ord(_)
        dodanie = numer + klucz
        zaszyfrowany = chr(dodanie)
        ostateczne += zaszyfrowany
    return(ostateczne)

print(szyfr_cezara(tekst, klucz))
        
        

        
        
        