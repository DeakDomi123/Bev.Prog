print("Adjon meg egy számot és egy mértékegységet (cm/inch):")
szam = input()
mertekegyseg = input()

if (mertekegyseg != "inch" and mertekegyseg != "cm"):
    print("Not correct unit!")
elif (mertekegyseg == "cm"):
    print(round((float(szam)*0.393700787),2)," inches")
elif (mertekegyseg == "inch"):
    print(round((float(szam)*2.54),2)," cm")