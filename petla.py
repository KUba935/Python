lp = 1

petla = True

while (petla == True):
    for i in range(1, 12):
        if i == 11:
            lp = lp + 1
            i = 1
        if lp == 11:
            petla = False
        else:
            m = lp * i
            print(f'Tabliczka mnożenia dla {lp} - {m}')


