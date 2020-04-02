from Vjezbe_2.stvar import Stvar
from Vjezbe_2.razlomak2 import Razlomak
print("*** TEST 1 ****")

s1 = Stvar()
s2 = Stvar()
s3 = s2
print(Stvar.brojStvari)
del (s2)
print(Stvar.brojStvari)
del (s3)
print(Stvar.brojStvari)
del (s1)
print(Stvar.brojStvari)


print('*** test 1 ***')
r1 = Razlomak(314,100)
r2 = Razlomak.inverz(r1)
print(r1,r2,r1)

print("*** test 2 ***")
r3 = Razlomak.stvori(3.14)
print(r3)
r4 = Razlomak.stvori(0.006021)
print(r4)
r5 = Razlomak.stvori(-75.204)
print(r5)