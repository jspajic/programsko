class Polje(object):

     def __init__(self, broj = 0):
          self.__broj = broj

     @property
     def vratiBroj(self):
          return self.__broj

     @property
     def jePrazno(self):
          if self.__broj == 0:
               return True
          else:
               return False
     @property
     def jeBroj(self):
          if self.__broj != 0:
               return True
          else:
               return False

     def __str__(self):
          if self.jeBroj == True:
               return '%d' % self.__broj
          if self.jePrazno == True:
               return ' '

     def __repr__(self):
          return 'Polje(%s)' % (self.__broj)

print('*** test 1 ***')
brojevi = list(range(9))
for broj in brojevi:
     polje = Polje(broj)
     print(polje.vratiBroj, polje.jeBroj, polje.jePrazno)

print('*** test 2 ***')
polja = [Polje(broj) for broj in range(9)]
for polje in polja:
     print(repr(str(polje)), repr(polje))