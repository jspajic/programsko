from Vjezbe_3.multiskup import MultiSkup

print('*** test 1 ***')
a = MultiSkup([1,1,2,2,2,3,3,4])
print(a)

print('*** test 2 ***')
a = MultiSkup([1,1,2,2,2,3,3,4])
for el in a:
 print(el)
print(repr(a))

a.add(4)
print(a)
a.add(2,3)
print(a)
a.remove(4,2)
print(a)