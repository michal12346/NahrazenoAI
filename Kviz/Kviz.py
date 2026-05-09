# Kviz - ŠESTÁ VERZE

import random

def spustit_kviz():
    # Databáze 10 otázek: mix výběrových (volba) a otevřených (otevrena)
    otazky = [
        {"text": "Jaké je hlavní město ČR?", "moznosti": "a) Brno  b) Praha  c) Ostrava", "spravne": "b", "typ": "volba"},
        {"text": "Napiš jméno prvního čs. prezidenta:", "spravne": "Tomáš Garrigue Masaryk", "typ": "otevrena"},
        {"text": "Kolik je 5 + 5?", "moznosti": "a) 10  b) 12  c) 8", "spravne": "a", "typ": "volba"},
        {"text": "Jak se jmenuje naše galaxie?", "spravne": "Mléčná dráha", "typ": "otevrena"},
        {"text": "Která planeta je nejblíže Slunci?", "moznosti": "a) Venuše  b) Země  c) Merkur", "spravne": "c", "typ": "volba"},
        {"text": "Jak se jmenuje nejdelší řeka světa?", "spravne": "Amazonka", "typ": "otevrena"},
        {"text": "Jaký chemický prvek má značku O?", "moznosti": "a) Zlato  b) Kyslík  c) Olovo", "spravne": "b", "typ": "volba"},
        {"text": "Napiš hlavní město Francie:", "spravne": "Paříž", "typ": "otevrena"},
        {"text": "V jakém roce skončila 2. sv. válka?", "moznosti": "a) 1945  b) 1939  c) 1918", "spravne": "a", "typ": "volba"},
        {"text": "Kdo napsal hru R.U.R.?", "spravne": "Karel Čapek", "typ": "otevrena"}
    ]

    # Hlavní smyčka pro možnost opakování hry
    while True:
        random.shuffle(otazky)
        skore = 0
        
        # Iterace přes seznam otázek
        for otazka in otazky:
            print("-" * 20)
            print(otazka["text"])
            
            # Dynamické zobrazení podle typu
            if otazka["typ"] == "volba":
                print(otazka["moznosti"])
                odpoved = input("Tvoje volba (a/b/c): ")
            else:
                odpoved = input("Tvoje odpověď: ")

            # Robustní kontrola shody textu
            if odpoved.lower().strip() == otazka["spravne"].lower().strip():
                print(">>> Správně!")
                skore += 1
            else:
                print(f">>> Špatně! Správně bylo: {otazka['spravne']}")
        
        # Závěrečné vyhodnocení
        print("\n" + "=" * 25)
        print(f"KVÍZ DOKONČEN! Skóre: {skore} / {len(otazky)}")
        print("=" * 25)

        if input("Chceš hrát znovu? (ano/ne): ").lower().strip() != "ano":
            print("Nashledanou!")
            break

if __name__ == "__main__":
    spustit_kviz()
