# Kviz - DEVÁTÁ VERZE

import random
import time

def spustit_kviz():
    # Finální rozsáhlá databáze: 15 otázek (volby, otevřené i časovky)
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
        {"text": "Kdo napsal hru R.U.R.?", "spravne": "Karel Čapek", "typ": "otevrena"},
        # Nové otázky
        {"text": "Který savec umí jako jediný aktivně létat?", "spravne": "netopýr", "typ": "otevrena"},
        {"text": "Který z těchto programovacích jazyků používáme pro tento kvíz?", "moznosti": "a) Java  b) Python  c) C++", "spravne": "b", "typ": "volba"},
        # Časovky
        {"text": "RYCHLOVKA: Kolik je 7 * 8?", "spravne": "56", "typ": "casovka", "limit": 10},
        {"text": "RYCHLOVKA: Jaká je chemická značka vody?", "spravne": "H2O", "typ": "casovka", "limit": 10},
        {"text": "RYCHLOVKA: Jaké je hlavní město Slovenska?", "spravne": "Bratislava", "typ": "casovka", "limit": 10}
    ]

    while True:
        random.shuffle(otazky)
        skore = 0
        
        for otazka in otazky:
            print("-" * 20)
            print(otazka["text"])
            
            if otazka["typ"] == "casovka":
                print(f"!!! POZOR, máš jen {otazka['limit']} sekund !!!")
                start_cas = time.time()
                odpoved = input("Tvoje odpověď: ")
                konec_cas = time.time()
                
                uplynuly_cas = konec_cas - start_cas
                
                if uplynuly_cas > otazka["limit"]:
                    print(f">>> Čas vypršel! Trvalo ti to {uplynuly_cas:.1f} s.")
                    print(f">>> Správně bylo: {otazka['spravne']}")
                    continue
            
            elif otazka["typ"] == "volba":
                print(otazka["moznosti"])
                odpoved = input("Tvoje volba (a/b/c): ")
            else:
                odpoved = input("Tvoje odpověď: ")

            if odpoved.lower().strip() == otazka["spravne"].lower().strip():
                print(">>> Správně!")
                skore += 1
            else:
                print(f">>> Špatně! Správně bylo: {otazka['spravne']}")
        
        print("\n" + "=" * 25)
        print(f"KVÍZ DOKONČEN! Skóre: {skore} / {len(otazky)}")
        print("=" * 25)

        if input("Chceš hrát znovu? (ano/ne): ").lower().strip() != "ano":
            print("Nashledanou!")
            break

if __name__ == "__main__":
    spustit_kviz()
