class Team:
    def __init__(self, nev, projekt, szerepkor):
        self._nev = nev
        self._projekt = projekt
        self._szerepkor = szerepkor
        print("-- Developer létrehozva. --")

    @property
    def szuperero(self):
        return self._projekt

    def __str__(self):
        return str(self._nev) + " a " + str(self._projekt) + "-en dolgozik " + str(self._szerepkor) + " szerepkörben."

    def __eq__(self, projekt):
        if self._projekt == projekt._projekt:
            return str(self._nev) + " és " + str(projekt._nev) + " dolgoznak egy projekten."

if __name__ == '__main__':
    dev1 = Team("Ricsi", "SolArch", "Frontend")
    print(dev1)
    dev2 = Team("Angéla", "ZerTeng", "Tesztelő")
    print(dev2)
    dev3 = Team("Peti", "KefERP", "Backend")
    print(dev3)
    dev4 = Team("Éva", "KefERP", "Frontend")
    print(dev4)
    print()
    lista = [dev1, dev2, dev3, dev4]
    szotar = {

    }
    for x in lista:
        szotar[x._projekt] = ""
    for x in lista:
        if x._nev not in szotar.values():
            szotar[x._projekt] = str(szotar[x._projekt]) + " " + str(x._nev)
    for x in szotar.values():
        if x.count(' ') > 1:
            valt1 = x.split(' ')
    print(valt1[2] + " és " + valt1[1] + " dolgoznak egy projekten.")