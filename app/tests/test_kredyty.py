import unittest
from app.Konto import Konto
from app.KontoFirmowe import KontoFirmowe


class TestKredyty(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Mariusz"
    pesel = "68451234856"

    nazwa = "Zabka"
    nip = "765-345-12-44"

    def setUp(self):
        self.konto = Konto(self.imie, self.nazwisko, self.pesel)

    def test_5_przelewy(self):
        self.konto.historia = [-100, 100, 100, 100, 600]
        czy_przyznany = self.konto.zaciagnij_kredyt(500)
        self.assertTrue(czy_przyznany)
        self.assertEqual(self.konto.saldo, 500, "Kredyt nie dodany do konta")

    def test_pusta_historia(self):
        self.konto.saldo = 0
        self.konto.historia = []
        czy_przyznany = self.konto.zaciagnij_kredyt(500)
        self.assertFalse(czy_przyznany, "Udzielono kredytu wbrew zasadom")
        self.assertEqual(self.konto.saldo, 0, "Udzielono kredytu wbrew zasadom")

    def test_za_krotka_historia(self):
        self.konto.historia = [-100, 50]
        czy_przyznany = self.konto.zaciagnij_kredyt(500)
        self.assertFalse(czy_przyznany, "Udzielono kredytu wbrew zasadom")
        self.assertEqual(self.konto.saldo, 0, "Udzielono kredytu wbrew zasadom")

    def test_same_wychodzace(self):
        self.konto.historia = [-100, -200, -4555, -412, -111]
        czy_przyznany = self.konto.zaciagnij_kredyt(500)
        self.assertFalse(czy_przyznany, "Udzielono kredytu wbrew zasadom")
        self.assertEqual(self.konto.saldo, 0, "Udzielono kredytu wbrew zasadom")

    def test_suma_mniejsza_niz_kredyt(self):
        self.konto.historia = [50, 30, 20, 10, 50, 10, 11]
        czy_przyznany = self.konto.zaciagnij_kredyt(2000000)
        self.assertFalse(czy_przyznany, "Udzielono kredytu osobie z zbyt małymi wpłatami")
        self.assertEqual(self.konto.saldo, 0, "Udzielono kredytu wbrew zasadom")
