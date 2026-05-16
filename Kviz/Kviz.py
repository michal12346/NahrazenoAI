# Kviz - SEDMÁ VERZE

import random
import time

def spustit_kviz():
    otazky = [
        {"text": "Jaké je hlavní město ČR?", "moznosti": "a) Brno  b) Praha  c) Ostrava", "spravne": "b", "typ": "volba"},
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
