def bekeres():
    print("Adja meg a háromszög oldalait cm-ben")
    a = int(input("a oldal (cm): "))
    b = int(input("b oldal (cm): "))
    c = int(input("c oldal (cm): "))
    return a, b, c


def szamitas():
    if(a + b > c and b + c > a and a + c > b):
        szerkesztheto = "A {}, {} és {} oldalú háromszög szerkeszthető."
        print(szerkesztheto.format(a,b,c))
    else:
        szerkesztheto = "A {}, {} és {} oldalú háromszög NEM szerkeszthető."
        print(szerkesztheto.format(a, b, c))


if __name__ == "__main__":
    a, b, c = bekeres()
    szamitas()
