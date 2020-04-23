from math import sqrt


class Trokut(object):
    def __init__(self, a, b, c):
        self.__stranice = (a, b, c)
        for stranica in self.__stranice:
            if stranica <= 0 or (self.__stranice[0] + self.__stranice[1]) <= self.__stranice[2]:
                raise ValueError("Nije trokut!")

    def __str__(self):
        string = "trokut "
        for stranica in self.__stranice:
            string += " " + str(stranica)

        return str(string)

    def __repr__(self):
        return "Trokut" + repr(self.__stranice)

    def opseg(self):
        opseg = 0
        for str in self.__stranice:
            opseg += str

        return opseg

    def povrsina(self):
        s = self.opseg() / 2
        return sqrt((s - self.__stranice[0]) * (s - self.__stranice[1]) * (s - self.__stranice[2]))


class JednakokracniTrokut(Trokut):
    def __init__(self, duljinaBaze, duljinaKraka):
        Trokut.__init__(self, duljinaBaze, duljinaKraka, duljinaKraka)


class JednakostranicniTrokut(JednakokracniTrokut):
    def __init__(self, stranica):
        JednakokracniTrokut.__init__(self, stranica, stranica)