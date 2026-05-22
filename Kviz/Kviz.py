# Kviz - DESÁTÁ VERZE

import random
import time

def spustit_kviz():
    otazky = [
        {"text": "Jaké je hlavní město ČR?", "moznosti": ["Praha", "Brno", "Ostrava"], "spravne": "Praha", "typ": "volba"},
        {"text": "RYCHLOVKA: Kolik je 7 * 8?", "spravne": "56", "typ": "casovka", "limit": 10},
        {"text": "Jak se jmenuje naše galaxie?", "spravne": "Mléčná dráha", "typ": "otevrena"}
    ]

    print("=== VÍTEJ V PARÁDNÍM KVÍZU ===")
    # Vyžádáme si jméno hráče. Tento řádek je mimo hlavní 'while' smyčku, takže se spustí jen jednou na začátku.
    jmeno_hrace = input("Zadej své jméno nebo přezdívku: ").strip()
    
    # Proměnná pro ukládání nejvyššího dosaženého skóre. Na začátku je to 0.
    osobni_rekord = 0

    while True:
        random.shuffle(otazky)
        skore = 0
        
        for otazka in otazky:
            print("-" * 30)
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
                aktualni_moznosti = otazka["moznosti"].copy()
                random.shuffle(aktualni_moznosti)
                pismena = ["a", "b", "c"]
                pismeno_spravne_odpovedi = ""
                
                for index, moznost in enumerate(aktualni_moznosti):
                    pismenko = pismena[index]
                    print(f"{pismenko}) {moznost}")
                    if moznost == otazka["spravne"]:
                        pismeno_spravne_odpovedi = pismenko
                
                odpoved = input("Tvoje volba (a/b/c): ").lower().strip()
                kontrola_spravnosti = pismeno_spravne_odpovedi
            else:
                odpoved = input("Tvoje odpověď: ")
                kontrola_spravnosti = otazka["spravne"]

            if odpoved.lower().strip() == kontrola_spravnosti.lower().strip():
                print(">>> Správně!")
                skore += 1
            else:
                if otazka["typ"] == "volba":
                    print(f">>> Špatně! Správná volba byla: {kontrola_spravnosti}) {otazka['spravne']}")
                else:
                    print(f">>> Špatně! Správně bylo: {otazka['spravne']}")
        
        # --- KONTROLA A AKTUALIZACE REKORDU ---
        # Pokud je skóre z právě dohraného kola vyšší než dosavadní rekord, přepíšeme ho
        if skore > osobni_rekord:
            osobni_rekord = skore
            print("\n*** SKVĚLE! TO JE TVŮJ NOVÝ OSOBNÍ REKORD! ***")

        print("\n" + "=" * 35)
        # Použijeme jméno hráče a jeho osobní rekord v závěrečném shrnutí
        print(f"Hráč: {jmeno_hrace}")
        print(f"Skóre v tomto kole: {skore} / {len(otazky)}")
        print(f"Tvůj osobní rekord: {osobni_rekord} / {len(otazky)}")
        print("=" * 35)

        if input("Chceš hrát znovu? (ano/ne): ").lower().strip() != "ano":
            print(f"Díky za hru, {jmeno_hrace}! Měj se hezky.")
            break

if __name__ == "__main__":
    spustit_kviz()
