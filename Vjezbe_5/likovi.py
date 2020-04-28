class Kruznica():

    def __init__(self, radijus):
        self.__radijus = radijus

    @property
    def radijus(self):
        return self.__radijus

    @radijus.setter
    def radijus(self, radijus):
        self.__radijus = radijus

    def __str__(self):
        return "kruznica radijusa %.2f" % (self.__radijus)


class Kvadrat():
    def __init__(self, duljinaStranice):
        self.__duljinaStranice = duljinaStranice

    @property
    def duljinaStranice(self):
        return self.__duljinaStranice

    @duljinaStranice.setter
    def duljinaStranice(self, duljinaStranice):
        self.__duljinaStranice = duljinaStranice

    def __str__(self):
        return "kvadrat stranice %.2f" % (self.__duljinaStranice)


if __name__ == "__main__":
    print('*** test likovi ***')
    kruznica = Kruznica(3)
    kvadrat = Kvadrat(4.5)
    print(kruznica)
    print(kvadrat)
