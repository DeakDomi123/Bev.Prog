def szotarfeltoltes(bekertmondat):
    for x in bekertmondat:
        if (szotar.__contains__(x)):
            szotar[x] += 1
        else:
            szotar[x] = 1

def bekeres():
    print("Adjon meg egy mondatot:")
    bekertmondat = input()
    return bekertmondat

if __name__ == "__main__":
    bekertmondat = bekeres()
    szotar = {

    }
    szotarfeltoltes(bekertmondat)
    print("Betűk gyakorisága: ",szotar)
    print("Fordítva: ",bekertmondat[::-1])
    lista = bekertmondat.split(' ')
    print("Listába rendezve szavanként: ",lista)