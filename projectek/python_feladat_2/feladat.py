# A feladatok megoldásánál nem végzek tipusellenőrzést, nem vizsgálok határértékeket.

# 1. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a
# legkisebb értéket ezek közül!
def legkisebb():
    szam1, szam2, szam3 = input("Adj meg három számot: ").split()
    eredmeny = min(int(szam1), int(szam2), int(szam3))
    print(f"A három beírt szám közül a legkisebb: {eredmeny}")

# 2. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a
# legnagyobb értéket ezek közül!
def legnagyobb():
    szam1, szam2, szam3 = input("Adj meg három számot: ").split()
    eredmeny = max(int(szam1), int(szam2), int(szam3))
    print(f"A három beírt szám közül a legkisebb: {eredmeny}")

# 3. Írj egy Python programot, amely bekér egy dolgozat pontszámot (x) a felhasználótól és kiír egy
# érdemjegyet az alábbiak szerint! 1: x<50; 2: 50<=x<60; 3: 60<=x<70; 4: 70<=x<85; 5: x>=85.
def dolgozat_pontszam():
    beker = int(input("Adj meg egy dolgozat pontszámot: "))
    if beker < 50:
        print("osztályzat: 1")
        return 
    elif beker >= 50 and beker < 60:
        print("osztályzat: 2")
        return
    elif beker >= 60 and beker < 70:
        print("osztályzat: 3")
        return 
    elif beker >= 70 and beker < 85:
        print("osztályzat: 4")
        return
    elif beker >= 85:
        print("osztályzat: 5")
        return
        
# 4. Írj egy Python programot, amely bekér egy egész számot a felhasználótól és kiírja a képernyőre,
# hogy osztható-e (igen/nem) a szám 3-mal vagy 5-tel!
def oszthato_e_harom():
    beker = int(input("kérek egy egész számot: "))
    if beker%3 == 0:
        print("A megadott szám osztható hárommal")
    if beker%5 == 0:
        print("A megadott szám osztható öttel")

# 5. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre,
# hogy a számok közül bármelyik kettőnek az összege egyenlő-e a harmadik számmal!
def harom_szam_melyik_ketto_osszege_harmadik():
    szam1, szam2, szam3 = input("Adj meg három számot: ").split()
    szam1 = int(szam1)
    szam2 = int(szam2)
    szam3 = int(szam3)

    if szam1 + szam2 == szam3:
        print("az első és második szám összege megegyezik a harmadikkal")
    if szam1 + szam3 == szam2:
        print("az első és harmadik szám összege megegyezik a másodikkal")
    if szam2 + szam3 == szam1:
        print("a második és a harmadik szám összege megegyezik az elsővel")

# 6. Írj egy Python programot, amely bekér három egész számot a felhasználótól és kiírja a
# képernyőre, hogy mind a három páros szám-e (igen/nem)!
def harom_paros_e():
    szam1, szam2, szam3 = input("Adj meg három számot: ").split()
    szam1 = int(szam1)
    szam2 = int(szam2)
    szam3 = int(szam3)
    
    if szam1 % 2 == 0 and szam2 % 2 == 0 and szam3 % 2 == 0:
        print("mindhárom szám páros")
    else:
        print("nem mind a három szám páros")

# 7. Írj egy Python programot, amely bekér két szót (sztringet) a felhasználótól és ABC sorrendben
# kiírja őket a képernyőre!
def ket_szo():
    szavak = input("Adj meg két szót: ").split()
    
    print("A megadott szavak abc sorrendben: ")
    szavak.sort()
    for e in szavak:
        print(e)

# 8. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a
# képernyőre azokat a pozitív hárommal osztható számokat, amelyek kisebbek az adott számnál!

def kisebb_harommal_oszthato():
    beker = int(input("Adj meg egy pozitív egész számot: "))

    print("A beírt számnál kisebb, hárommal osztható pozitív egész számok: ")
    for i in range(beker-1, 0, -1):
        if i%3 == 0:
           print(i)

# 9. Írj egy Python programot, amely bekér két pozitív egész számot a felhasználótól és kiírja a
# képernyőre azokat a páros számokat, amelyek a két adott érték közötti zárt intervallumban
# találhatóak!

def ket_egesz_kozott_paros():
    szam1, szam2 = input("Adj meg két egész számot: ").split()
    szam1 = int(szam1)
    szam2 = int(szam2)

    print("A két egész szám között található páros egész számok: ")
    
    for i in range(min(szam1, szam2)+1, max(szam1, szam2)-1):
        if i % 2 == 0:
            print(i)

# 10. Írj egy Python programot, amely bekér egy 20-nál nem nagyobb pozitív egész számot a
# felhasználótól és kiírja a képernyőre a START szót úgy, hogy előtte annyi szóköz legyen amennyi
# a megadott szám értéke!
def start():
    beker = int(input("Adj egy 20 -nál nem nagyobb pozitív egész számot: "))
    print(" "*beker, "START")


# legkisebb()
# legnagyobb()
# dolgozat_pontszam()
# oszthato_e_harom()
# harom_szam_melyik_ketto_osszege_harmadik()
# harom_paros_e()
# ket_szo()
# kisebb_harommal_oszthato()
# ket_egesz_kozott_paros()
# start()

