from Vjezbe_5.likovi import *
from math import pi


def opseg(lik):
    if isinstance(lik, Kvadrat):
        return 4 * lik.duljinaStranice
    elif isinstance(lik, Kruznica):
        return 2 * lik.radijus * pi


def povrsina(lik):
    if isinstance(lik, Kvadrat):
        return pow(lik.duljinaStranice, 2)
    elif isinstance(lik, Kruznica):
        return pow(lik.radijus, 2) * pi

if __name__ == "__main__":
    print('*** test funkcije ***')
    print(opseg.__name__)
    print(povrsina.__name__)