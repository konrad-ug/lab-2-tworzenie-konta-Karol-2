import unittest

from app.Konto import Konto
from app.RejestrKont import RejestrKont


class TestRejestrKont(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "89495784261"

    @classmethod
    def setUpClass(cls):# pierwsze konto
        konto = Konto(cls.imie,cls.nazwisko,cls.pesel)
        RejestrKont.dodaj_konto(konto)

    def test_1_dodawanie_drugiego_konta(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        RejestrKont.dodaj_konto(konto)
        self.assertEqual(RejestrKont.ile_kont(),2)

    def test_2_dodawanie_trzeciego_konta(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        RejestrKont.dodaj_konto(konto)
        self.assertEqual(RejestrKont.ile_kont(),3)

    def test_3_szukanie_konta(self):
        szukany_pesel = "89495784261"
        self.assertEqual(RejestrKont.wyszukaj_konto(szukany_pesel).pesel,szukany_pesel)

    @classmethod
    def tearDownClass(cls):
        RejestrKont.konta = []
