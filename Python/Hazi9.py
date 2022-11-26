if __name__ == '__main__':
    lista = [2, 5, 6, 8, 13, 32, 42, 50, 53, 62, 66, 70, 80, 89, 91]
    N = len(lista)
    also, felso, lepesszam = 0, N - 1, 0
    while also <= felso:
        k = (felso + also)//2
        lepesszam += 1
        if 70 < lista[k]:
            felso = k - 1
        elif 70 > lista[k]:
            also = k + 1
        else:
            kimenet = lepesszam, also, felso, k
            break
    print("A 70-es értéket " + str(kimenet[0]) + " lépésben találta meg, " + str(kimenet[1]) + " alsó értékkel, " +
          str(kimenet[2]) + " felső értékkel és " + str(kimenet[3]) + " k értékkel." )