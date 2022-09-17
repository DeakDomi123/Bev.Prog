print("Adjon meg egy mondatot:")
bekertmondat = input()
szotar = {

}

for x in bekertmondat:
    if (szotar.__contains__(x)):
        szotar[x] += 1
    else:
        szotar[x] = 1

print("Betűk gyakorisága: ",szotar)
print("Fordítva: ",bekertmondat[::-1])

lista = bekertmondat.split(' ')
print("Listába rendezve szavanként: ",lista)