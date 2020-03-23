class Razlomak(object):
    """
    Brojnik i nazivnik se šalju kao argumenti tijekom inicijalizacije klase
    Napravi svojstva za čitanje i pisanje brojnika i nazivnika.
    Napravi metodu skrati() koja će skratiti razlomak, na primjer. razlomak 3/12 se može skratiti na 1/4

    U klasi razlomak napravi specijalnu metodu __str__() koja će služiti za ispis razlomka u obliku
    brojnik|nazivnik i specijalnu metodu __repr__() za reprezentaciju razlomka.
    Napravi specijalne metode za operacije usporedbe razlomaka.

    U klasi razlomak napravi specijalnu metode za zbrajanje, oduzimanje, množenje i dijeljenje razlomaka.
    """

    def __init__(self, brojnik, nazivnik):
        self._brojnik = brojnik
        self._nazivnik = nazivnik

    @property
    def brojnik(self):
        return self._brojnik

    @brojnik.setter
    def brojnik(self, value):
        self._brojnik = value

    @property
    def nazivnik(self):
        return self._nazivnik

    @nazivnik.setter
    def nazivnik(self, value):
        self._nazivnik = value

    def __repr__(self):
        return "Razlomak(" + repr(self._brojnik) + ", " + repr(self._nazivnik) + ")"

    def __str__(self):
        return str(self._brojnik) + "|" + str(self._nazivnik)

    def skratiRazlomak(self):
        nzd = None
        manjiBroj = self._brojnik if self._brojnik < self._nazivnik else self._nazivnik

        for broj in range(2, int(manjiBroj + 1)):
            if (self._brojnik % broj == 0 and self._nazivnik % broj == 0):
                nzd = broj

        if (nzd == None):
            return str(self)
        else:
            self._brojnik //= nzd
            self._nazivnik //= nzd
            # print("Razlomak je skracen i iznosi: " + str(self))

    """
        Usporedbe
    """

    def __eq__(self, other):
        return (self.brojnik / self.nazivnik) == (other._brojnik / other._nazivnik)

    def __lt__(self, other):
        return (self.brojnik / self.nazivnik) < (other.brojnik / other.nazivnik)

    def __ge__(self, other):
        return (self.brojnik / self.nazivnik) >= (other.brojnik / other.nazivnik)

    """
        Zbrajanje, oduzimanje, množenje i dijeljenje razlomaka.
    """

    def __add__(self, other):
        brojnik = (self.brojnik * other.nazivnik) + (other.brojnik * self.nazivnik)
        nazivnik = self.nazivnik * other.nazivnik

        return str(Razlomak(brojnik, nazivnik))

    def __sub__(self, other):

        if (self.nazivnik == other.nazivnik):
            brojnik = self.brojnik - other.brojnik
            nazivnik = self.nazivnik
        else:
            brojnik = (self.brojnik * other.nazivnik) - (other.brojnik * self.nazivnik)
            nazivnik = self.nazivnik * other.nazivnik

        return Razlomak(brojnik, nazivnik)

    # kod mul i truediv funkcije automatski se skracuje razlomak
    def __mul__(self, other):
        brojnik = self.brojnik * other.brojnik
        nazivnik = self.nazivnik * other.nazivnik

        razlomak = Razlomak(brojnik, nazivnik)
        razlomak.skratiRazlomak()

        return razlomak

    def __truediv__(self, other):
        brojnik = self.brojnik * other.nazivnik
        nazivnik = self.nazivnik * other.brojnik

        razlomak = Razlomak(brojnik, nazivnik)
        razlomak.skratiRazlomak()

        return razlomak
