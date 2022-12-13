# A példa feladatokbanf nem végzek semmilyen, valós programok esetén szükséges
# vizsgálatot a bekért adatokkal kapcsolatban.

# 0. Írj egy Python programot, amely bekér egy 20-nál nem nagyobb pozitív egész számot a
# felhasználótól és kiírja a képernyőre a START szót úgy, hogy előtte annyi szóköz legyen amennyi
# a megadott szám értéke! 
def start():
    beker = int(input("Adj egy 20 -nál nem nagyobb pozitív egész számot: "))
    print(" "*beker, "START")

# 1. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a
# képernyőre azt a számot, amely az ennél a számnál nem nagyobb pozitív egész számok
# összege! 
def nem_nagyobb_pozitiv_egesz_szamok():
    beker = int(input("Adj meg egy pozitív egész számot: "))
    szamok = range(beker + 1)
    print("az ennél a számnál nem nagyobb pozitív egész számok összege: ", sum(szamok))

# 2. Írj egy Python programot, amely bekér egy szót (sztringet) a felhasználótól és kiírja a
# képernyőre a szó betűit, úgy, hogy minden betű egy új sorba kerüljön! 
def minden_betu_uj_sorban():
    beker = input("Adj meg egy szót: ")
    for e in beker:
        print(e)

# 3. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a
# képernyőre felváltva a 0 és 1 számjegyeket úgy, hogy a számjegyek együttes darabszáma
# pontosan a megadott szám legyen! 
def felvaltva_nulla_egy():
    beker = int(input("Adj meg egy egész számot: "))
    sz = False
    for _ in range(beker):
        print(int(sz), end='')
        sz = not sz

# 4. Írj egy Python programot, amely először bekér egy kisebb majd egy nagyobb pozitív valós
# számot a felhasználótól és kiírja a képernyőre azokat az egész számokat, amelyek a megadott
# értékek között helyezkednek el!
def ket_egesz_kozott():
    # bekéréskor valós számok
    beker1 = float(input("Adj meg egy pozitív valós számot: "))
    beker2 = float(input("Adj meg még egy pozitív valós számot: "))
    
    # továbbiakban egészként, csak lefele
    beker1 = int(beker1)
    beker2 = int(beker2)

    print("az egész számok, amelyek a megadott értékek között helyezkednek el!")
    for i in range(min(beker1, beker2)+1, max(beker1, beker2)):
        print(i)

# 5. Írj egy Python eljárást, amely paraméterként kap 2 egész számot (N és M) és kiír a képernyőre
# a csillag (*) karaktereket M darab sorban és N darab oszlopban (tehát NxM darab karaktert egy
# téglalap alakú képernyőrészre)! A programodban hívd is meg ezt az alprogramot!
def negyzet(a, b):
    for _ in range(a):
        print("*"*b)

# start()
# nem_nagyobb_pozitiv_egesz_szamok()
# minden_betu_uj_sorban()
felvaltva_nulla_egy()
# ket_egesz_kozott()
# negyzet(20, 40)