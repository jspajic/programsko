import json
import sqlite3

class Ispiti(dict):

    def dodaj(self, student, kolegij, ocjena):
        if student not in self:
            self[student] = {}
        self[student][kolegij] = ocjena

    def izbrisi(self, student, kolegij):
        if kolegij in self[student]:
            self[student].pop(kolegij)


    def promijeni(self, student, kolegij, ocjena):
        self[student][kolegij] = ocjena


    def spremi_datoteka(self, naziv_datoteke):
        with open(naziv_datoteke, "w", encoding='utf-8') as datoteka:
            for student, kolegij in self.items():
                for kol, ocj in kolegij.items():
                    datoteka.write("%s \t %s \t %s \n" % (student, kol, str(ocj)))

    def spremi_json(self, naziv_datoteke):
        with open(naziv_datoteke, "w", encoding="utf8") as datoteka:
            json.dump(self, datoteka)

    @staticmethod
    def ucitaj_json(datoteka):
        with open(datoteka, "r", encoding="utf8") as datoteka:
            isp = Ispiti(json.load(datoteka))
            return isp