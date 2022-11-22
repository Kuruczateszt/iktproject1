import random

def jo_napod_van_e():
    ered = ""
    while ered not in ["igen", "nem"]:
        ered = input("Jó napod van? (igen, nem) ")
        print("Sajnos nem értem a válaszodat!")

    if ered == "igen":
        print("Örülök hogy jó napod van")
    else:
        print("Sajnálom hogy rossz napod van")
    
def paros_e():
    ered = None
    while ered is None:
        try:
            ered = int(input("adj meg egy egész számot: "))
        except ValueError:
            print("csak számokat adhatsz meg: ")

    if ered % 2 != 0:
        print("A beírt szám páratlan")
    else:
        print("A beírt szám páros")

def gondoltam_egy_szamra():
    gondol = random.randrange(1, 6)
    ered = None 
    while ered is None:
        szam = None
        try:
            szam = int(input("Adj meg egy számot 1 és 5 között: "))
        except ValueError:
            print("csak számokat adhatsz meg: ")
            continue
        if szam not in [1, 2, 3, 4, 5]:
            print("Nem megfelelő számot adtál meg")
        else:
            ered = szam

    print(f"Az általad megadott szám az {ered}")
    if ered == gondol:
        print("Kitaláltad a gép által gondolt számot")
    elif ered < gondol:
        print("A gép nagyobb számra gondolt")
    else:
        print("A gép kisebb számra gondolt")


def paros_egy_es_tiz_kozott():
    szamok = list(range(1, 11))
    
    for szam in szamok:
        if szam % 2 == 0:
            print(szam)

def egytol_tizig_csokkeno():
    szamok = list(range(10, 0, -1))
    for szam in szamok:
        print(szam)

def paratlan_egy_es_tiz_kozott_csokkeno():
    szamok = list(range(10, 0, -1))
    for szam in szamok:
        if szam % 2 != 0:
            print(szam)

def szoveg_kiir_db():
    kiirando = input("Adj meg egy tetszőleges szöveget: ")
    db = None

    while db is None:
        szam = None
        try:
            szam = int(input("Add meg hányszor szeretnéd kiírni: "))
        except ValueError:
            print("Csak egész számokat adhatsz meg: ")
            continue
        if szam < 0:
            print("Csak pozitív számot adhatsz meg")
        else:
            db = szam

    for i in range(db):
        print(f"{i+1}: {kiirando}")

def paros_szam_vizsgal():
    ered = None

    while ered is None:
        szam = None
        try:
            szam = int(input("Adj meg egy páros egész számot"))
        except ValueError:
            print("Csak egész számokat adhatsz meg: ")
            continue
        if szam % 2 != 0:
            print("Csak páros számot adhatsz meg")
        else:
            ered = szam

    print(f"A megadott páros szám: {ered}")

def veletlenszeru_szamok():
    veletlen_szamok = []
    db = 0
    for i in range(21):
        veletlen_szamok.append(random.randrange(1, 13))

    for ertek in veletlen_szamok:
        if ertek % 3 == 0:
            db += 1
    
    print(f"hárommal oszthatók darabszáma: {db}")

# jo_napod_van_e()
# paros_e()
# gondoltam_egy_szamra()
# paros_egy_es_tiz_kozott()
# egytol_tizig_csokkeno()
# paratlan_egy_es_tiz_kozott_csokkeno()
# szoveg_kiir_db()
# paros_szam_vizsgal()
veletlenszeru_szamok()
