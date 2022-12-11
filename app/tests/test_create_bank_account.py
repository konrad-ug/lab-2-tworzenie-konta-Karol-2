import unittest
from app.Konto import Konto


class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "89495784261"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.pesel, "89495784261", "Pesel nie został zapisany!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_pesel_za_krotki(self):
        za_krotki_pesel = "911"
        konto_klienta = Konto(self.imie, self.nazwisko, za_krotki_pesel)
        self.assertEqual(konto_klienta.pesel, "Niepoprawny pesel!")

    def test_pesel_za_dlugi(self):
        za_dlugi_pesel = "123456751545542351311"
        konto_klienta = Konto(self.imie, self.nazwisko, za_dlugi_pesel)
        self.assertEqual(konto_klienta.pesel, "Niepoprawny pesel!")

    def test_dobry_kod_rabatowy(self):
        dobry_kod = "PROM_5G3"
        konto_klienta = Konto(self.imie, self.nazwisko, self.pesel, dobry_kod)
        self.assertEqual(konto_klienta.saldo, 50, "Nie dodano pieniędzy za akcję promocyjną do salda!")

    def test_zly_kod_rabatowy(self):
        niepoprawny_kod = "MORP_666"
        konto_klienta = Konto(self.imie, self.nazwisko, self.pesel, niepoprawny_kod)
        self.assertEqual(konto_klienta.saldo, 0, "Saldo początkowe nie jest równe zero")

    def test_kod_rabatowy_i_pesel_seniora(self):
        senior_pesel = "50123456784"
        konto_klienta = Konto(self.imie, self.nazwisko, senior_pesel)
        self.assertEqual(konto_klienta.saldo, 0, "Seniorowi naliczono promocję!")
