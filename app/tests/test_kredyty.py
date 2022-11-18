import unittest
from app.Konto import Konto
from app.KontoFirmowe import KontoFirmowe

from parameterized import parameterized


class TestKredyty(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Mariusz"
    pesel = "68451234856"

    nazwa = "Zabka"
    nip = "765-345-12-44"

    def setUp(self):
        self.konto = Konto(self.imie, self.nazwisko, self.pesel)

    @parameterized.expand([
        ([-100, 100, 100, 100, 600], 500, True, 500),
        ([], 500, False, 0),
        ([-100, 50], 500, False, 0),
        ([-100, -200, -4555, -412, -111], 500, False, 0),
        ([50, 30, 20, 10, 50, 10, 11], 200000, False, 0)
    ])
    def test_5_przychodzace_przelewy(self, historia, kwota_kredytu, oczekiwany_wynik, oczekiwane_saldo):
        self.konto.historia = historia
        czy_przyznany = self.konto.zaciagnij_kredyt(kwota_kredytu)
        self.assertEqual(czy_przyznany, oczekiwany_wynik)
        self.assertEqual(self.konto.saldo, oczekiwane_saldo)
