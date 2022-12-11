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
        return None

    @classmethod
    def usun_konto(cls, pesel):
        konto = cls.wyszukaj_konto(pesel)
        if konto:
            cls.konta.remove(konto)
            return True
        return None

    @classmethod
    def ile_kont(cls):
        return len(cls.konta)
