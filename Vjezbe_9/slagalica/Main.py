from Vjezbe_9.slagalica.Ploca import Ploca

print('*** test 1 ***')
broj_redova, broj_stupaca = 3, 3
polje = Ploca(broj_redova, broj_stupaca)
print(polje.vratiVelicinuPloce(), polje.vratiBrojPolja())
print()
polje.postaviPlocu([0, 8, 7, 6, 5, 4, 3, 2, 1])
for red in polje._Ploca__polja:
    for n in red:
        print(n, end = '|')
    print()


print('\n*** test 2 ***')
polje = Ploca(3, 4)
polje.postaviPlocu([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0])
print(polje)
for n in polje:
    print(n, repr(n))

