import unittest
from app.KontoFirmowe import KontoFirmowe


class TestTworzeniaKontaFirmowego(unittest.TestCase):
    nazwa = "Żabka"
    nip = "123-456-78-91"

    def test_tworzenie_konta_firmowego(self):
        pierwsze_konto_firmowe = KontoFirmowe(self.nazwa, self.nip)
        self.assertEqual(pierwsze_konto_firmowe.nazwa, "Żabka", "Nazwa nie została zapisana")
        self.assertEqual(pierwsze_konto_firmowe.nip, "123-456-78-91", "NIP nie został został zapisany")
        self.assertEqual(pierwsze_konto_firmowe.saldo, 0, "Saldo nie jest zerowe!")

    def test_za_krotki_NIP(self):
        zly_NIP = "455"
        pierwsze_konto_firmowe = KontoFirmowe(self.nazwa, zly_NIP)
        self.assertEqual(pierwsze_konto_firmowe.nip, "Niepoprawny NIP!", "Zły nip został zapisany")

    def test_NIP_z_myslnikami(self):
        myslniki_NIP = "455-234-12-12"
        pierwsze_konto_firmowe = KontoFirmowe(self.nazwa, myslniki_NIP)
        self.assertEqual(pierwsze_konto_firmowe.nip, "455-234-12-12", "Nie akceptuje NIP z myślnikami")

    def test_NIP_bez_myslnikow(self):
        czysty_NIP = "4552341212"
        pierwsze_konto_firmowe = KontoFirmowe(self.nazwa, czysty_NIP)
        self.assertEqual(pierwsze_konto_firmowe.nip, "4552341212", "Nie akceptuje NIP bez myslników")
