class Stvar(object):

    brojStvari = 0

    def __init__(self):
        Stvar.brojStvari += 1

    def __del__(self):
        Stvar.brojStvari -= 1