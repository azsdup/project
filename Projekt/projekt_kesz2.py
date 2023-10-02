import random

also_hatar = None
felso_hatar = None
szovegek_darabszama = None

def menu():
    global also_hatar, felso_hatar, szovegek_darabszama
    while True:
        print("Válasszon egy lehetőséget: \n")
        print("1. Véletlen számok generálása és kiírása")
        print("2. Véletlen szövegek generálása és kiírása")
        print("3. Számok ellenőrzése a 'ki.txt' állományban")
        print("4. Szövegek ellenőrzése a 'ki.txt' állományban")
        print("0. Kilépés \n")
        valasztas = input("Kérem válasszon (0-4): \n")
        
        if valasztas == '1':
            also_hatar = int(input("Adja meg az alsó határt: "))
            felso_hatar = int(input("Adja meg a felső határt: "))
            while felso_hatar <= also_hatar:
                print("A felső határ nem lehet kisebb vagy egyenlő az alsó hattárnál.")
                felso_hatar = int(input("Adja meg újra a felső határt: "))
            generalt_szamok()
        
        elif valasztas == '2':
            szovegek_darabszama = int(input("Adja meg a generálandó szövegek darabszámát: "))
            generalt_szovegek()
        
        elif valasztas == '3':
            eredmeny = ellenorzes_szamok()
            if eredmeny:
                print("A beolvasott számok megfelelnek a feltételeknek. \n")
            else:
                print("A beolvasott számok nem felelnek meg a feltételeknek. \n")
        
        elif valasztas == '4':
            eredmeny = ellenorzes_szovegek()
            if eredmeny:
                print("A beolvasott szövegek megfelelnek a feltételeknek. \n")
            else:
                print("A beolvasott szövegek nem felelnek meg a feltételeknek. \n")
        
        elif valasztas == '0':
            break
        
        else:
            print("Kérem válasszon újra.")

def generalt_szamok():
    darabszam = int(input("Adja meg a generálandó számok darabszámát: "))
    with open("ki.txt", "w") as f:
        for _ in range(darabszam):
            veletlen_szam = random.randint(also_hatar, felso_hatar)
            f.write(str(veletlen_szam) + ";")
    print("Generálva és kiírva a ki.txt állományba. \n")

def generalt_szovegek():
    abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    with open("ki.txt", "w") as f:
        for _ in range(szovegek_darabszama):
            hossz = random.randint(1, 20)
            szoveg = ''.join(random.choice(abc) for _ in range(hossz))
            f.write(szoveg + ";")
    print("Szövegek generálva és kiírva a ki.txt állományba. \n")

def ellenorzes_szamok():
    if also_hatar is None or felso_hatar is None:
        print("Először generáljon számokat az alsó és felső határok megadásával. \n")
        return False
    
    with open("ki.txt", "r") as f:
        szamok = f.readline().split(";")
    for szam in szamok:
        szam = szam.strip()
        if szam:
            szam = int(szam)
            if not (also_hatar <= szam <= felso_hatar):
                return False
    return True

def ellenorzes_szovegek():
    global szovegek_darabszama
    if szovegek_darabszama is None or szovegek_darabszama <= 0:
        print("Először adja meg a szövegek darabszámát a 2. pontban.")
        return False
    
    abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    with open("ki.txt", "r") as f:
        szovegek = f.readline().split(";")
    for szoveg in szovegek:
        szoveg = szoveg.strip()
        if szoveg:
            if not (1 <= len(szoveg) <= 20 and all(c in abc for c in szoveg)):
                return False
    return True

menu()
