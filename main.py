class film:
    def __init__(self, tytul="", liczba_wyporzyczen=0):
        self._tytul = tytul
        self._liczba_wyporzyczen = liczba_wyporzyczen

    def setTytul(self, value):
        self._tytul = value
        return self

    def getTytul(self):
        return self._tytul

    def getLiczbaWyporzyczen(self):
        return self._liczba_wyporzyczen

    def inkrementuj_wyporzyczenia(self):
        self._liczba_wyporzyczen += 1


if __name__ == "__main__":
    Obiekt = film()

    # Test metody set
    Obiekt.setTytul("Incepcja")
    print("Test setTytul ",Obiekt.getTytul())

    #  Test metody get
    print("Test getTytul",Obiekt.getTytul())

    # Test inkrementacji
    print("Przed", Obiekt.getLiczbaWyporzyczen())
    Obiekt.inkrementuj_wyporzyczenia()
    print("Po", Obiekt.getLiczbaWyporzyczen())