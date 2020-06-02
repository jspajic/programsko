class Razlomak():

    def __init__(self, brojnik, nazivnik=1):
        if nazivnik == 0: raise Exception('Nazivnik ne moze biti 0')
        self._brojnik = brojnik
        self._nazivnik = nazivnik

    def __str__(self):
        return '%d|%d' % (self._brojnik, self._nazivnik)

    @staticmethod
    def inverz(self):
        return Razlomak(self._nazivnik, self._brojnik)

    @staticmethod
    def stvori(number: float):
        _brojDecimala = str(number)[::-1].find('.')

        _nazivnik = 10 ** _brojDecimala
        _brojnik = int(number * _nazivnik)

        return Razlomak(_brojnik, _nazivnik)