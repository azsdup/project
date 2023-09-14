import random
def menu():
    while True:
        print("Válasszon egy lehetőséget:")
        print("1. Véletlen számok generálása és kiírása")
        print("2. Véletlen szövegek generálása és kiírása")
        print("3. Számok ellenőrzése a 'ki.txt' állományban")
        print("4. Szövegek ellenőrzése a 'ki.txt' állományban")
        print("0. Kilépés")
        valasztas=input("Kérem válasszon (0-4): ")
        if valasztas == '1':
            generalt_szamok()
        elif valasztas == '2':
            generalt_szovegek()
        elif valasztas == '3':
            ellenorzes_szamok()
        elif valasztas == '4':
            ellenorzes_szovegek()
        elif valasztas == '0':
            break
        else:
            print("Kérem válasszon újra.")
def generalt_szamok():
    also_hatar = int(input("Adja meg az alsó határt: "))
    felso_hatar = int(input("Adja meg a felső határt: "))
    darabszam = int(input("Adja meg a generálandó számok darabszámát: "))
    with open("ki.txt", "w") as f:
        for _ in range(darabszam):
            veletlen_szam = random.randint(also_hatar, felso_hatar)
            f.write(str(veletlen_szam) + ";\n")
    print("Generálva és kiírva a ki.txt állományba.")
def generalt_szovegek():
    darabszam = int(input("Adja meg a generálandó szövegek darabszámát: "))
    abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    with open("ki.txt", "w") as f:
        for _ in range(darabszam):
            hossz = random.randint(1, 20)
            szoveg = ''.join(random.choice(abc) for _ in range(hossz))
            f.write(szoveg + ";\n")
    print("Szövegek generálva és kiírva a ki.txt állományba.")

def ellenorzes_szamok():
    also_hatar = int(input("Adja meg az alsó határt: "))
    felso_hatar = int(input("Adja meg a felső határt: "))
    with open("ki.txt", "r") as f:
        szamok = f.readlines()
    for szam in szamok:
        szam=int(szam.strip(';'))
        if not (also_hatar <= szam <= felso_hatar):
            print(f"Hiba: {szam} nem felel meg a határoknak.")
def ellenorzes_szovegek():
    abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    with open("ki.txt", "r") as f:
        szovegek=f.readlines()
    for szoveg in szovegek:
        szoveg=szoveg.strip(';')
        if not (1 <= len(szoveg)<=20 and all(c in abc for c in szoveg)):
            print(f"Hiba: '{szoveg}' nem felel meg a feltételeknek.")
menu()
