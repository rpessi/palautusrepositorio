import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko()

    joukko.lisaa(1)
    joukko.lisaa(2)
    joukko.lisaa(3)
    print(joukko.to_int_list())
    joukko.lisaa(2)
    print(joukko.to_int_list())
    joukko.lisaa(5)
    print(joukko.to_int_list())
    joukko.poista(2)
    print(joukko.to_int_list())

if __name__ == "__main__":
    main()
