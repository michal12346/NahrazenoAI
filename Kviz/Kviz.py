# Kviz - DRUHÁ VERZE

otazky = {
    "Jaké je hlavní město ČR?": "Praha",
    "Kolik je 5 + 5?": "10"
}

# Proměnná pro uchování aktuálního skóre hráče
skore = 0

# Cyklus nyní rozbaluje slovník na 'otazka' a 'spravna_odpoved' (pomocí .items())
for otazka, spravna_odpoved in otazky.items():
    print(otazka)
    odpoved = input("Tvoje odpověď: ")
    
    # Podmínka pro kontrolu odpovědi. 
    # Funkce .lower() a .strip() zajišťují, že nebude vadit velká/malá písmena ani mezery navíc.
    if odpoved.lower().strip() == spravna_odpoved.lower():
        print("Správně!\n")
        skore += 1 # Zvýšení skóre o 1 bod
    else:
        print(f"Špatně! Správná odpověď byla: {spravna_odpoved}\n")
