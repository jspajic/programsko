import sqlite3
from Vjezbe_6.ispit import Ispiti


class IspitiDB():
    def __init__(self, baza):
        self.conn = sqlite3.Connection(baza)
        self.cur = self.conn.cursor()
        self.cur.executescript("""
                    DROP TABLE IF EXISTS ispiti;
                    DROP TABLE IF EXISTS kolegiji;
                    DROP TABLE IF EXISTS studenti;

                    CREATE TABLE studenti (
                        student_id integer PRIMARY KEY,
                        ime_prezime text NOT NULL UNIQUE);

                    CREATE TABLE kolegiji (
                        kolegiji_id integer PRIMARY KEY,
                        naziv text NOT NULL UNIQUE);

                    CREATE TABLE ispiti (
                        student_id integer,
                        kolegiji_id integer,
                        ocjena integer NOT NULL,
                        PRIMARY KEY (student_id, kolegiji_id),
                        FOREIGN KEY (student_id) REFERENCES studenti (student_id),
                        FOREIGN KEY (kolegiji_id) REFERENCES kolegiji (kolegiji_id));            
                    """)

    def vrati_kolegiji_id(self, naziv):
        self.cur.execute("""SELECT kolegiji_id FROM kolegiji WHERE naziv = ?""", (naziv,))
        row = self.cur.fetchone()
        if row:
            return row[0]

    def dodaj_kolegiji(self, naziv):
        self.cur.execute("""INSERT INTO kolegiji (naziv) VALUES (?)""", (naziv,))
        self.conn.commit()
        return self.cur.lastrowid

    def vrati_student_id(self, ime_prezime):
        self.cur.execute("""
        SELECT student_id FROM studenti WHERE ime_prezime = ? 
        """, (ime_prezime,))
        row = self.cur.fetchone()
        if row:
            return row[0]
        else:
            return "Student s imenom '" + ime_prezime + "' ne postoji!"

    def dodaj_student(self, ime_prezime):
        self.cur.execute("""
            INSERT INTO studenti (ime_prezime) VALUES (?)
        """, (ime_prezime,))

        self.conn.commit()
        return self.cur.lastrowid

    def promijeni_student(self, ime_prezime, novo_ime_prezime):
        student_id = self.vrati_student_id(ime_prezime)

        if student_id:
            self.cur.execute("""
                UPDATE studenti 
                SET ime_prezime = (?) 
                WHERE student_id = ?
            """, (novo_ime_prezime, student_id))

        self.conn.commit()

    def izbrisi_student(self, ime_prezime):
        student_id = self.vrati_student_id(ime_prezime)

        if student_id:
            self.cur.execute("""
                DELETE FROM studenti WHERE student_id = ?
            """, (student_id,))

    def svi_ispiti(self):
        self.cur.execute("""
            SELECT studenti.ime_prezime, kolegiji.naziv, ispiti.ocjena
            FROM studenti
            INNER JOIN ispiti ON studenti.student_id = ispiti.student_id
            INNER JOIN kolegiji ON kolegiji.kolegiji_id = ispiti.kolegiji_id
        """)

        isp = Ispiti()
        for i in self.cur.fetchall():
            isp.dodaj(i[0], i[1], i[2])

        return isp

    def ispitaj(self, student, kolegij, ocjena=None):
        # fetch da vidmo postoji li taj ispit

        self.cur.execute("""
            SELECT * FROM ispiti WHERE student_id = (?) AND kolegij_id = (?)"
        """, self.vrati_student_id(student), self.vrati_kolegiji_id(kolegij))

        ispit = self.cur.fetchone()
        # Provjeriti postoje li student i/ili kolegij
        if isinstance(db.vrati_student_id(student), str):
            self.dodaj_student(student)

        if isinstance(db.vrati_kolegiji_id(kolegij), str):
            self.dodaj_kolegiji(student)

        if ocjena == None:
            if ispit:
                self.cur.execute("""
                                DELETE FROM ispiti WHERE student_id = (?)
                                AND kolegij_id = (?)
                            """, self.vrati_student_id(student), self.vrati_kolegiji_id(kolegij))

                self.conn.commit()
        else:
            if ispit:
                self.cur.execute("""
                            UPDATE ispiti SET ocjena = (?) WHERE student_id = (?) AND kolegiji_id = (?)
                """,
                 (ocjena, self.vrati_student_id(student), self.vrati_kolegiji_id(kolegij)))
                self.conn.commit()
            else:
                self.cur.execute("""
                            INSERT INTO ispiti (student_id, kolegiji_id, ocjena) 
                            VALUES (?, ?, ?
                """,
                (self.vrati_student_id(student), self.vrati_kolegiji_id(kolegij), ocjena))
                self.conn.commit()
