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

    marad = ered % 2
    if marad != 0:
        print("A beírt szám páratlan")
    else:
        print("A beírt szám páros")

# jo_napod_van_e()
paros_e()
