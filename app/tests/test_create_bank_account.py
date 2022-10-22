import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    imie = "Dariusz"
    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, "Januszewski", "12345678912")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, "12345678912","Zly pesel")

