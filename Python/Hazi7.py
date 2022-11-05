def Palindrom():
    szo = str(input("Kérem a mondatot: "))
    szo = szo.lower()
    # Írásjelek és szóközök eltörlése
    szo = szo.replace(" ", "").replace("?", "").replace("!", "").replace(".", "").replace(",", "").replace("-", "")\
        .replace(":", "")
    # Hosszú magánhangzók eltávolítása
    szo = szo.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ő", "ö")\
        .replace("ú", "u").replace("ű", "ü")
    # Mássalhangzók kezelése
    szo = szo.replace("ssz", "Z1Z").replace("sz", "HH").replace("zs", "HH")

    szo2 = szo
    # Mássalhangzók felcserélése a vizsgálat segítéséhez
    szo2 = szo2.replace("cs", "sc").replace("dz", "zd").replace("dzs", "szd").replace("gy", "yg").replace("ly", "yl")\
        .replace("ny", "yn").replace("ty", "yt")
    palindrom = True
    szamolo = len(szo) - 1
    for x in szo:
        if x == szo2[szamolo]:
            palindrom = True
        else:
            palindrom = False
            break
        szamolo = szamolo - 1
    if palindrom:
        print("A mondat/szó palindróm")
    else:
        print("A mondat/szó nem palindróm")


if __name__ == '__main__':
    Palindrom()