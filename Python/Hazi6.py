def megjelenit():
    elrendezes = "\t{0:>5}{1:>5}{2:>5}{3:>5}{4:>5}{5:>5}{6:>5}{7:>5}{8:>5}{9:>5}{10:>5}{11:>5}"
    print(elrendezes.format("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"))
    print(" :--------------------------------------------------------------")
    for i in range(1, 13):
        print(str(i) + ":" + elrendezes.format(i, i * 2, i * 3, i * 4, i * 5, i * 6, i * 7, i * 8, i * 9, i * 10, i * 11, i * 12))



if __name__ == '__main__':
    megjelenit()