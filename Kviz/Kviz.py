# Kviz - FINÁLNÍ VERZE

# Hlavní funkce, která obaluje celou logiku kvízu, aby kód nebyl jen volně v souboru
def spustit_kviz():
    otazky = {
        "Jaké je hlavní město ČR?": "Praha",
        "Kolik je 5 + 5?": "10",
        "Která planeta je nejblíže Slunci?": "Merkur"
    }

    skore = 0
    
    # Cyklus prochází každou otázku a porovnává vstupy
    for otazka, spravna_odpoved in otazky.items():
        print(otazka)
        odpoved = input("Tvoje odpověď: ")
        
        # Ošetření vstupů pro spravedlivé vyhodnocení
        if odpoved.lower().strip() == spravna_odpoved.lower():
            print("Správně!\n")
            skore += 1
        else:
            print(f"Špatně! Správná odpověď byla: {spravna_odpoved}\n")
    
    # Výpočet a zobrazení celkové úspěšnosti pomocí funkce len() (délka slovníku)
    celkem_otazek = len(otazky)
    print("-------------------------")
    print(f"Konec kvízu! Tvé skóre: {skore} z {celkem_otazek}")

# Speciální podmínka v Pythonu. 
# Zajišťuje, že se funkce 'spustit_kviz' spustí pouze tehdy, když je tento skript spuštěn přímo.
if __name__ == "__main__":
    spustit_kviz()
