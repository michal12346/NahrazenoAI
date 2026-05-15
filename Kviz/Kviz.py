# Kviz - SEDMÁ VERZE

import random
import time # Importujeme modul pro práci s časem

def spustit_kviz():
    # Zatím přidáme jen jednu ukázkovou časovku, abychom otestovali logiku
    otazky = [
        {"text": "Jaké je hlavní město ČR?", "moznosti": "a) Brno  b) Praha  c) Ostrava", "spravne": "b", "typ": "volba"},
        {"text": "RYCHLOVKA: Kolik je 7 * 8?", "spravne": "56", "typ": "casovka", "limit": 10}
    ]

    while True:
        random.shuffle(otazky)
        skore = 0
        
        for otazka in otazky:
            print("-" * 20)
            print(otazka["text"])
            
            # Zpracování nového typu otázky "casovka"
            if otazka["typ"] == "casovka":
                print(f"!!! POZOR, máš jen {otazka['limit']} sekund !!!")
                
                start_cas = time.time() # Zaznamená aktuální čas před zadáním
                odpoved = input("Tvoje odpověď: ")
                konec_cas = time.time() # Zaznamená čas po stisknutí Enter
                
                uplynuly_cas = konec_cas - start_cas # Vypočítá, jak dlouho to trvalo
                
                # Pokud to trvalo déle, než je limit, rovnou skočíme na další otázku
                if uplynuly_cas > otazka["limit"]:
                    # .1f znamená, že vypíšeme čas zaokrouhlený na 1 desetinné místo
                    print(f">>> Čas vypršel! Trvalo ti to {uplynuly_cas:.1f} s.")
                    print(f">>> Správně bylo: {otazka['spravne']}")
                    continue # Příkaz continue přeskočí zbytek cyklu a jde na další otázku
            
            # Zpracování klasických otázek
            elif otazka["typ"] == "volba":
                print(otazka["moznosti"])
                odpoved = input("Tvoje volba (a/b/c): ")
            else:
                odpoved = input("Tvoje odpověď: ")

            # Společné vyhodnocení pro včasné odpovědi
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
