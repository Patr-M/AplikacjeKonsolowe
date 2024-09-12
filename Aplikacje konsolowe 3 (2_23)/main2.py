class Notatka:
    __countingNotes = 0
    def __init__(self, title="", content=""):
        Notatka.__countingNotes += 1
        self.__id = Notatka.__countingNotes
        self._title = title
        self._content = content

    def ShowANote(self):
        return "Tytuł "+self._title+" -> Treść "+self._content

    def Diagnose(self):
        return str(self.__id) + ";" + self._title + ";" + self._content
if __name__ == "__main__":
    notatka1 = Notatka("Zakupy", "Kalafior, Kapusta, Chleb")
    notatka2 = Notatka("Kalendarz", "Lekarz na 15, Spotkanie na 17")
    print("\n",notatka1.ShowANote())
    print("\n",notatka1.Diagnose())
    print("\n",notatka2.ShowANote())
    print("\n",notatka2.Diagnose())