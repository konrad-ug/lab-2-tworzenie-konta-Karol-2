class RejestrKont:
    konta = []

    @classmethod
    def dodaj_konto(cls, konto):
        cls.konta.append(konto)

    @classmethod
    def wyszukaj_konto(cls, pesel):
        for account in cls.konta:
            if account.pesel == pesel:
                return account
            else:
                return None

    @classmethod
    def usun_konto(cls,pesel):
        konto = cls.wyszukaj_konto(pesel)
        cls.konta.remove(konto)

    @classmethod
    def ile_kont(cls):
        return len(cls.konta)
