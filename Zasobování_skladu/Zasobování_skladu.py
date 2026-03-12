 Simulátor skladu - FINÁLNÍ VERZE
# Práce s více položkami a logické vyhodnocení

# Nastavení počátečních hodnot pro dva druhy zboží
telefony = 100
notebooky = 50
limit = 10

pokracovat = "ano"
while pokracovat == "ano":
    print("\n--- DENNÍ PŘEHLED ZÁSOB ---")
    print(f"Telefony: {telefony} ks | Notebooky: {notebooky} ks")
    
    # Simulace prodejů pomocí vstupů
    prodano_tel = int(input("Prodaných telefonů dnes: "))
    prodano_ntb = int(input("Prodaných notebooků dnes: "))
    
    # Logika odečtu s kontrolou, aby stav nebyl záporný
    # Využití funkce max() zajistí, že nejnižší hodnota bude 0
    telefony = max(0, telefony - prodano_tel)
    notebooky = max(0, notebooky - prodano_ntb)
    
    # Komplexní vyhodnocení stavu skladu (Větvení)
    if telefony < limit and notebooky < limit:
        print("!!! KRITICKÝ STAV: Celý sklad je téměř prázdný!")
    elif telefony < limit or notebooky < limit:
        print("UPOZORNĚNÍ: Jedna z položek dochází.")
    else:
        print("Vše v pořádku, zásob je dostatek.")
        
    pokracovat = input("Chceš simulovat další den? (ano/ne): ")

print("--- KONEC SIMULACE ---")
