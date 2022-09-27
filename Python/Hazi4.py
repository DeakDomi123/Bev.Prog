def kiszamolo(szam1, szam2):
    return szam1/szam2


if __name__ == '__main__':
    while True:
        a = int(input("Enter 'a' value: "))
        b = int(input("Enter 'b' value: "))
        try:
            print(kiszamolo(a, b))
        except ZeroDivisionError:
            print("Division by zero not allowed")
        print("Out of try except blocks")