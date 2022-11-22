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

# jo_napod_van_e()
# paros_e()
# gondoltam_egy_szamra()
# paros_egy_es_tiz_kozott()
# egytol_tizig_csokkeno()
paratlan_egy_es_tiz_kozott_csokkeno()
