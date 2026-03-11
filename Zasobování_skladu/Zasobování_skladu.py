# Simulátor skladu - 2 VERZE
# Přidáno hlídání maximální kapacity

kapacita_skladu = 500
aktualni_zasoby = 100
minimalni_limit = 20

pokracovat = "ano"
while pokracovat == "ano":
    # Výpočet procentuálního zaplnění pro lepší přehlednost
    procento_zaplneni = (aktualni_zasoby / kapacita_skladu) * 100
    print(f"\nSklad je zaplněn z {procento_zaplneni}% ({aktualni_zasoby}/{kapacita_skladu} ks)")
    
    prijato = int(input("Kolik kusů chcete naskladnit: "))
    
    # Logika kontroly kapacity - zaměřeno na přetečení skladu
    if aktualni_zasoby + prijato > kapacita_skladu:
        print("!!! CHYBA: Tolik zboží se sem nevejde!")
        print(f"Můžeš naskladnit maximálně {kapacita_skladu - aktualni_zasoby} ks.")
    else:
        aktualni_zasoby += prijato
        print("Zboží úspěšně naskladněno.")
        
    pokracovat = input("Chceš pokračovat? (ano/ne): ")
