def bekeres():
    print("Adjon meg egy számot és egy mértékegységet (cm/inch):")
    szam = int(input())
    mertekegyseg = input()
    return szam,mertekegyseg

def kiszamolo(szam, mertekegyseg):
    if (mertekegyseg == "cm"):
        print(round((szam*0.393700787),2)," inches")
    elif (mertekegyseg == "inch"):
        print(round((szam*2.54),2)," cm")
    elif (mertekegyseg != "inch" and mertekegyseg != "cm"):
        print("Not correct unit!")

if __name__ == "__main__":
    szam,mertekegyseg = bekeres()
    kiszamolo(szam,mertekegyseg)