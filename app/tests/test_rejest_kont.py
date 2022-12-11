import unittest

from app.Konto import Konto
from app.RejestrKont import RejestrKont


class TestRejestrKont(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "89495784261"

    @classmethod
    def setUpClass(cls):  # pierwsze konto
        konto = Konto(cls.imie, cls.nazwisko, cls.pesel)
        RejestrKont.dodaj_konto(konto)

    def test_1_dodawanie_drugiego_konta(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        RejestrKont.dodaj_konto(konto)
        self.assertEqual(RejestrKont.ile_kont(), 2, "nie dodano drugiego konta")

    def test_2_dodawanie_trzeciego_konta(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        RejestrKont.dodaj_konto(konto)
        self.assertEqual(RejestrKont.ile_kont(), 3, "nie dodano trzeciego konta")

    def test_3_szukanie_konta(self):
        szukany_pesel = "89495784261"
        self.assertEqual(RejestrKont.wyszukaj_konto(szukany_pesel).pesel, szukany_pesel, "błąd w szukaniu pesela")

    def test_4_szukanie_nieistniejacego_konta(self):
        szukany_pesel = "11111111111"
        self.assertEqual(RejestrKont.wyszukaj_konto(szukany_pesel), None, "znaleziono błędny pesel")

    def test_5_usuwanie_konta(self):
        usuwanie_konta = RejestrKont.usun_konto(self.pesel)
        self.assertTrue(usuwanie_konta)

    def test_6_usuwanie_nieistniejacego_konta(self):
        usuwanie_konta = RejestrKont.usun_konto("99999999999")
        self.assertIsNone(usuwanie_konta)

    @classmethod
    def tearDownClass(cls):
        RejestrKont.konta = []
