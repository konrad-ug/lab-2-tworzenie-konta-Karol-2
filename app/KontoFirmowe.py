from app.Konto import Konto


class KontoFirmowe(Konto):
    def __init__(self, nazwa, nip):
        self.nazwa = nazwa
        self.saldo = 0
        self.SprawdzanieNIP(nip)

    def SprawdzanieNIP(self, NIP):
        if sum(a.isdigit() for a in NIP) == 10:
            self.nip = NIP
        else:
            self.nip = "Niepoprawny NIP!"
