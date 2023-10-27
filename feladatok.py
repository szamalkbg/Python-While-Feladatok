def feladat1():
    szm1 = 0
    while szm1 <= 150:
        if szm1 % 2 == 0:
            print(szm1, end=", ")
        szm1 += 1

def feladat2():
    haromoszthato = 0
    sorszam = 1

    while sorszam < 10:
        szam2 = int(input("Adja meg a(z) "+str(sorszam)+". számot: "))
        if szam2 % 3 == 0:
            haromoszthato += 1
        sorszam += 1
    print("A bekért számok alapján "+str(haromoszthato)+" olyan szám található, amely 3-mal osztható.")

def feladat3():
    szam3 = int(input("Adjon meg egy számot:"))
    while szam3 % 10 != 0:
        szam3 = int(input("Adjon meg egy számot:"))
    print("A bekért szám 10-el osztható! Gratulálunk nyertél egy ajándékcsomagot!")
    return szam3

def feladat4():
    szam4 = int(input("Kérlek, adj meg egy számot: "))
    while not ((szam4 >= 10 and szam4 < 100) or (szam4 <= -10 and szam4 > -100)) and szam4 % 2 != 0:
        szam4 = int(input("Kérlek, adj meg egy számot: "))
    print("A megadott kétjegyű, páros szám: ", szam4, "Gratulálunk nyertél egy ajándékcsomagot!")
    return szam4


def feladat5():
    szam5 = int(input("Kérlek, adj meg egy számot: "))
    while not (szam5 > 0 and szam5 % 2 == 1):
        szam5 = int(input("Kérlek, adj meg egy számot: "))
    print("A megadott pozitív páratlan szám:", szam5, "Gratulálunk nyertél egy ajándékcsomagot!")
    return szam5

def feladat6():
    szam6 = int(input("Kérlek adj meg egy számot: "))
    while not (szam6 % 3 == 0 or szam6 **0.5 % 1 == 0):
        szam6 = int(input("Kérlek adj meg egy számot: "))
    print("A megadott 3-al osztható néégyzetszám:", szam6, "Gratulálunk nyertél egy ajándékcsomagot!")
    return szam6

def feladat7():
    a = int(input("Add meg a háromszög a oldalát: "))
    b = int(input("Add meg a háromszög b oldalát: "))
    c = int(input("Add meg a háromszög c oldalát: "))
    while not ((a + b > c) and (a + c > b) and (b + c > a)):
        a = int(input("Add meg a háromszög a oldalát: "))
        b = int(input("Add meg a háromszög b oldalát: "))
        c = int(input("Add meg a háromszög c oldalát: "))
    print("A megadott oldalak alapján létezik háromszög! ")

def feladat8():
    szoveg1 = input("Kérlek, adj meg egy szöveget: ")
    while not len(szoveg1) > 3:
        szoveg1 = input("Kérlek, adj meg egy szöveget: ")
    print(szoveg1.upper(), "Gratulálunk nyertél egy ajándékcsomagot!")

def feladat9():
    szoveg2 = input("Kérlek adj meg egy szöveget: ")
    while not (len(szoveg2) == 4 and szoveg2.islower()):
        szoveg2 = input("Kérlek, adj meg egy szöveget: ")
    print(szoveg2, "Gratulálunk nyertél egy ajándékcsomagot!")

def feladat10():
    osszeg = 0
    darab = 0
    szam = int(input("Kérlek, adj meg egy egész számot (0 jelzi a befejezést): "))
    while szam != 0:
        osszeg += szam
        darab += 1
        szam = int(input("Kérlek, adj meg egy egész számot (0 jelzi a befejezést): "))
    if darab > 0:
        atlag = osszeg / darab
        print("Az átlag: {:.2f}".format(atlag))
    else:
        print("Nem adtál meg számot.")

def feladat11():

    osszeg11 = 0
    darab11 = 0
    szam11 = float(input("Kérlek, adj meg egy pozitív számot (0 jelzi a befejezést): "))
    while szam11 != 0 and szam11 > 0:
        osszeg11 += szam11
        darab11 += 1
        szam11 = float(input("Kérlek, adj meg egy egész számot (0 jelzi a befejezést): "))
    if darab11 > 0:
        atlag = osszeg11 / darab11
        print("Az átlag: {:.2f}".format(atlag))
    else:
        print("Nem adtál meg számot, vagy nem pozitív számot adtál meg!")