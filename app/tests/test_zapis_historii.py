import unittest
from app.Konto import Konto
from app.KontoFirmowe import KontoFirmowe


class TestZapisHistorii(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Mariusz"
    pesel = "68451234856"

    nazwa = "Zabka"
    nip = "765-345-12-44"

    def test_zapis_historii_klient(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.zaksieguj_przelew_przychodzacy(6000)
        konto.zaksieguj_przelew_wychodzacy(5500)
        konto.zaksieguj_przelew_przychodzacy(300)
        self.assertEqual(konto.historia, [6000, -5500, 300], "Niepoprawna historia dla przelewów zwykłych, klient")

    def test_zapis_historii_ekspresowe_klient(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.zaksieguj_przelew_przychodzacy(6000)
        konto.przelew_express_wychodzacy(500)
        konto.zaksieguj_przelew_przychodzacy(300)
        self.assertEqual(konto.historia, [6000, -500, -1, 300],
                         "Niepoprawna historia dla przelewów ekspresowych, klient")

    def test_zapis_historii_firma(self):
        konto = KontoFirmowe(self.nazwa, self.nip)
        konto.zaksieguj_przelew_przychodzacy(6000)
        konto.zaksieguj_przelew_wychodzacy(5500)
        konto.zaksieguj_przelew_przychodzacy(300)
        self.assertEqual(konto.historia, [6000, -5500, 300], "Niepoprawna historia dla przelewów zwykłych, firma")

    def test_zapis_historii_ekspresowe_firma(self):
        konto = KontoFirmowe(self.nazwa, self.nip)
        konto.zaksieguj_przelew_przychodzacy(6000)
        konto.przelew_express_wychodzacy(5500)
        konto.zaksieguj_przelew_przychodzacy(300)
        self.assertEqual(konto.historia, [6000, -5500, -5, 300],
                         "Niepoprawna historia dla przelewów ekspresowych, firma")
