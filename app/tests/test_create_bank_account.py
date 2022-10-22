import unittest

from ..Konto import Konto


class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678912"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.pesel, "12345678912", "Pesel nie został zapisany!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_pesel(self):
        za_krotki_pesel = "911"
        konto_klienta = Konto(self.imie, self.nazwisko, za_krotki_pesel)
        self.assertEqual(konto_klienta.pesel, "Niepoprawny pesel!")

        za_dlugi_pesel = "123456751545542351311"
        konto_klienta = Konto(self.imie, self.nazwisko, za_dlugi_pesel)
        self.assertEqual(konto_klienta.pesel, "Niepoprawny pesel!")

    def test_kupon_rabatowy(self):
        senior_pesel = "50123456784"
        mlody_pesel = "89495784261"

        dobry_kod = "PROM_5G3"
        konto_klienta = Konto(self.imie, self.nazwisko, mlody_pesel, dobry_kod)
        self.assertEqual(konto_klienta.saldo, 50, "Nie dodano pieniędzy za akcję promocyjną do salda!")

        niepoprawny_kod="MORP_666"
        konto_klienta = Konto(self.imie, self.nazwisko, mlody_pesel, niepoprawny_kod)
        self.assertEqual(konto_klienta.saldo, 0, "Saldo początkowe nie jest równe zero")

        konto_klienta = Konto(self.imie, self.nazwisko,senior_pesel)
        self.assertEqual(konto_klienta.saldo, 0, "Seniorowi naliczono promocję!")



