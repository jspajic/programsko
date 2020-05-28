from Vjezbe_9.Mine.Polje import Polje

polje = Polje(5, 2)
for red in polje._Polje__kvadrati:
    for n in red:
        n.otkrij()
        print(n, end=' | ')
    print()

print('\n*** test 2 ***')
print('*** rezultat varira zbog slucajnog izbora mina koristenjem random modula ***')
polje = Polje(5, 2)
for red in polje._Polje__kvadrati:
    for n in red:
        n.otkrij()
print(polje)
