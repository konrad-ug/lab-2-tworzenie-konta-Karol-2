import unittest
import requests


class TestObslugaKonta(unittest.TestCase):
    body = {
        "imie": "nick",
        "nazwisko": "cave",
        "pesel": "01292909876"
    }

    body_zmienione = {
        "imie": "Jarosław",
        "nazwisko": "Kaczka",
        "pesel": "82123052241"
    }

    url = "http://localhost:5000"

    def test_1_tworzenie_kont_poprawnie(self):
        create_resp = requests.post(self.url + "/konta/stworz_konto", json=self.body)
        self.assertEqual(create_resp.status_code, 201)

    def test_2_tworzenie_drugiego_konta_na_ten_sam_pesel(self):
        create_resp = requests.post(self.url + "/konta/stworz_konto", json=self.body)
        self.assertEqual(create_resp.status_code, 400)
    def test_3_znajdz_konto_po_peselu(self):
        get_resp = requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(get_resp.status_code, 200)
        resp_body = get_resp.json()
        self.assertEqual(resp_body["nazwisko"], self.body["nazwisko"])
        self.assertEqual(resp_body["imie"], self.body["imie"])
        self.assertEqual(resp_body["saldo"], 0)

    def test_4_zmiana_danych(self):
        put_resp = requests.put(self.url + f"/konta/aktualizuj/{self.body['pesel']}", json=self.body_zmienione)
        self.assertEqual(put_resp.status_code, 200)
        resp_body = put_resp.json()
        self.assertEqual(resp_body["imie"], self.body_zmienione["imie"])
        self.assertEqual(resp_body["nazwisko"], self.body_zmienione["nazwisko"])
        self.assertEqual(resp_body["pesel"], self.body_zmienione["pesel"])

    def test_5_usuwanie_konta(self):
        delete_resp = requests.delete(self.url + f"/konta/usun/{self.body_zmienione['pesel']}")
        self.assertEqual(delete_resp.status_code, 200)

    def test_6_usuwanie_konta_nieistniejacego(self):
        delete_resp = requests.delete(self.url + f"/konta/usun/47101226256")
        self.assertEqual(delete_resp.status_code, 404)

