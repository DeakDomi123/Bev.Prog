if __name__ == '__main__':
    with open("Files/hazi.txt", "r", encoding="utf8") as f:
        sorok = []
        for sor in f:
            if not sor == "\n":
                sorok.append(sor.replace(" ", "").replace(".", "").replace(",", "").replace(":", "").replace(";", "")
                             .replace("!", "").replace("?", "").replace("'", '').replace('"', '').replace("-", "")
                             .replace("a", "").replace("á", "").replace("e", "").replace("é", "").replace("i", "")
                             .replace("í", "").replace("o", "").replace("ó", "").replace("ö", "").replace("ő", "")
                             .replace("u", "").replace("ú", "").replace("ü", "").replace("ű", "").replace("A", "")
                             .replace("Á", "").replace("E", "").replace("É", "").replace("I", "").replace("Í", "")
                             .replace("O", "").replace("Ó", "").replace("Ö", "").replace("Ő", "")
                             .replace("U", "").replace("Ú", "").replace("Ü", "").replace("Ű", ""))

        szamlalo = 1
        with open("Files/Rozsikimenet.txt", "w", encoding="utf8") as f2:
            for sor in sorok:
                if szamlalo % 3 == 0:
                    f2.write(sor)
                szamlalo = szamlalo + 1