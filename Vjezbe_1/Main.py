from Vjezbe_1.razlomak import Razlomak

print('*** test 1 ***')
r1 = Razlomak(3, 5)
print(r1.brojnik, r1.nazivnik)
r1.skratiRazlomak()
print(r1.brojnik, r1.nazivnik)

print('*** test 2 ***')
r1 = Razlomak(12, 30)
r2 = Razlomak(2, 5)
r3 = Razlomak(3, 6)
print(r1, r2, repr(r3))
print(r1 == r2)
print(r3 >= r1)
print(r3 < r2)

print('*** test 3 ***')
print(Razlomak(3, 4) + Razlomak(5, 2))
print(Razlomak(4,4)-Razlomak(2,4))
print(Razlomak(2,8)*Razlomak(4,2))
print(Razlomak(2,3)/Razlomak(4,5))