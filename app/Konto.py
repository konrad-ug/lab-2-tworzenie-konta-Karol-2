class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = None
        self.saldo = 0

        self.sprawdz_pesel(pesel)
        self.sprawdz_kod_rabatowy(kod_rabatowy)

    def sprawdz_pesel(self, pesel):
        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"

    def sprawdz_kod_rabatowy(self, kod):
        if kod is not None:
            if len(kod) == 8 and kod[0:5] == "PROM_":  # warunki feature4
                if int(self.pesel[0:2]) > 60:  # warunki feature 5
                    self.saldo += 50
