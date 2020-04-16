class MultiSkup():

    def __init__(self, multiSkup = None):
        self._multiSkup = multiSkup
        self._kljucevi = {}

        self._jedinstveneVrijednosti = []

        for i in self._multiSkup:
            if i not in self._jedinstveneVrijednosti:
                self._jedinstveneVrijednosti.append(i)

        for i in self._jedinstveneVrijednosti:
            self._kljucevi[i] = self._multiSkup.count(i)

    def __str__(self):
        printable = []

        for kljuc, vrijednost in self._kljucevi.items():
            printable.append(str(kljuc)+"*"+str(vrijednost))

        return "{{"+ ",".join(printable) +"}}"

    def __iter__(self):
        return iter(self._multiSkup)

    def __repr__(self):
        return "Multiskup(" + str(self._multiSkup) + ")"

    def add(self, key, value = None):
        if(key not in self._kljucevi.keys()):
            raise Exception("Nepostojeci kljuc")
        else:
            if value is None:
                self._kljucevi[key] += 1
            else:
                self._kljucevi[key] += value

    def remove(self, key, value=None):
        if (key not in self._kljucevi.keys()):
            raise Exception("Nepostojeci kljuc")
        else:
            if value is None:
                self._kljucevi[key] -= 1
            else:
                self._kljucevi[key] -= value
                if self._kljucevi[key] == 0:
                    del self._kljucevi[key]