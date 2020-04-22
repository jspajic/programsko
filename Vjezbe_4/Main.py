from Vjezbe_4.trokut import *

print('*** test 1 ***')
lista_stranica = [(1, 2, 3), (3, 4, 5), (3, 4, 4), (3, 3, 3)]
for stranice in lista_stranica:
    try:
        t = Trokut(*stranice)
        print(repr(t))
    except Exception as e:
        print(e, stranice)

print('*** test 2 ***')
lista_stranica = [(3,4,5),(3,4,4),(3,3,3)]
for stranice in lista_stranica:
     t = Trokut(*stranice)
     print('%r ima opseg %.3f i povrsinu %.3f' % (t, t.opseg(), t.povrsina()))

print('*** test 3 ***')
trokuti = [Trokut(3, 4, 5), JednakokracniTrokut(3, 4), JednakostranicniTrokut(5)]
for t in trokuti:
    print(t)