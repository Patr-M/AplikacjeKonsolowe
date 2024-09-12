class Osoba:
    countingInstances = 0
    def __init__(self, id=0,imie=""):
        self.__imie = imie
        self.__id = id
        Osoba.countingInstances += 1
        self.test = "bombaa"
    def CopyMethod(self,o):
        return Osoba(o.__id, o.__imie)

osoba1 = Osoba(1, "Adam")
osoba2 = osoba1.CopyMethod(osoba1)
osoba1.test = "Ale oko"
print(osoba1.__dict__)
print(osoba2.__dict__)
print(Osoba.countingInstances)