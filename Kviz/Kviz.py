# Kviz - DVACÁTÁPRVÁ VERZE

import random  
import time    

# Zde definujeme konstanty pro barvy pomocí ANSI escape sekvencí.
# Tímto říkáme terminálu, ať změní barvu vypisovaného textu.
ZELENA = '\033[92m'
CERVENA = '\033[91m'
ZLUTA = '\033[93m'
RESET = '\033[0m' # Tento kód vrátí barvu zpět na normální (výchozí).

def spustit_kviz():
    otazky = [
        # --- KATEGORIE 1: Geografie ---
        {"text": "Jaké je hlavní město ČR?", "moznosti": ["Praha", "Brno", "Ostrava"], "spravne": "Praha", "typ": "volba", "kategorie": "1"},
        {"text": "Jaká je nejvyšší hora České republiky?", "moznosti": ["Praděd", "Sněžka", "Lysá hora"], "spravne": "Sněžka", "typ": "volba", "kategorie": "1"},
        {"text": "Napiš hlavní město Francie:", "spravne": "Paříž", "typ": "otevrena", "kategorie": "1"},
        {"text": "Jak se jmenuje nejdelší řeka světa?", "spravne": "Amazonka", "typ": "otevrena", "kategorie": "1"},
        {"text": "Kolik kontinentů je tradičně na Zemi?", "moznosti": ["5", "6", "7"], "spravne": "7", "typ": "volba", "kategorie": "1"},
        {"text": "Který oceán je největší na světě?", "moznosti": ["Tichý", "Atlantský", "Indický"], "spravne": "Tichý", "typ": "volba", "kategorie": "1"},
        {"text": "Napiš hlavní město Itálie:", "spravne": "Řím", "typ": "otevrena", "kategorie": "1"},
        {"text": "Jaký je nejmenší stát světa?", "moznosti": ["Monako", "Vatikán", "San Marino"], "spravne": "Vatikán", "typ": "volba", "kategorie": "1"},
        {"text": "Na kterém kontinentu leží Egypt?", "moznosti": ["Asie", "Afrika", "Evropa"], "spravne": "Afrika", "typ": "volba", "kategorie": "1"},
        {"text": "Napiš jméno státu, který je naším východním sousedem:", "spravne": "Slovensko", "typ": "otevrena", "kategorie": "1"},

        # --- KATEGORIE 2: Věda a technika ---
        {"text": "Kolik je 5 + 5?", "moznosti": ["10", "12", "8"], "spravne": "10", "typ": "volba", "kategorie": "2"},
        {"text": "Která planeta je nejblíže Slunci?", "moznosti": ["Venuše", "Merkur", "Země"], "spravne": "Merkur", "typ": "volba", "kategorie": "2"},
        {"text": "Jaký chemický prvek má značku O?", "moznosti": ["Zlato", "Kyslík", "Olovo"], "spravne": "Kyslík", "typ": "volba", "kategorie": "2"},
        {"text": "Který savec umí jako jediný aktivně létat?", "spravne": "netopýr", "typ": "otevrena", "kategorie": "2"},
        {"text": "Který programovací jazyk používáme pro tento kvíz?", "moznosti": ["Java", "Python", "C++"], "spravne": "Python", "typ": "volba", "kategorie": "2"},
        {"text": "Který orgán pumpuje krev v lidském těle?", "spravne": "srdce", "typ": "otevrena", "kategorie": "2"},
        {"text": "Kolik je 12 * 12?", "moznosti": ["144", "124", "142"], "spravne": "144", "typ": "volba", "kategorie": "2"},
        {"text": "Jak se jmenuje galaxie, ve které se nachází Země?", "moznosti": ["Andromeda", "Mléčná dráha", "Sombrero"], "spravne": "Mléčná dráha", "typ": "volba", "kategorie": "2"},
        {"text": "Napiš chemickou značku pro zlato:", "spravne": "Au", "typ": "otevrena", "kategorie": "2"},
        {"text": "Kdo zformuloval teorii relativity?", "moznosti": ["Isaac Newton", "Albert Einstein", "Nikola Tesla"], "spravne": "Albert Einstein", "typ": "volba", "kategorie": "2"},

        # --- KATEGORIE 3: Rychlovky ---
        {"text": "RYCHLOVKA: Kolik je 7 * 8?", "spravne": "56", "typ": "casovka", "limit": 10, "kategorie": "3"},
        {"text": "RYCHLOVKA: Jaká je chemická značka vody?", "spravne": "H2O", "typ": "casovka", "limit": 10, "kategorie": "3"},
        {"text": "RYCHLOVKA: Jaké je hlavní město Slovenska?", "spravne": "Bratislava", "typ": "casovka", "limit": 10, "kategorie": "3"},
        {"text": "RYCHLOVKA: Kolik minut má jedna hodina?", "spravne": "60", "typ": "casovka", "limit": 10, "kategorie": "3"},
        {"text": "RYCHLOVKA: Napiš zkratku České republiky:", "spravne": "ČR", "typ": "casovka", "limit": 10, "kategorie": "3"},
        {"text": "RYCHLOVKA: Jaký je výsledek 100 / 4?", "spravne": "25", "typ": "casovka", "limit": 10, "kategorie": "3"},
        {"text": "RYCHLOVKA: Kolik nohou má pavouk?", "spravne": "8", "typ": "casovka", "limit": 10, "kategorie": "3"},
        {"text": "RYCHLOVKA: Jaký den v týdnu následuje po pátku?", "spravne": "sobota", "typ": "casovka", "limit": 10, "kategorie": "3"},
        {"text": "RYCHLOVKA: Napiš oficiální zkratku pro Evropskou unii:", "spravne": "EU", "typ": "casovka", "limit": 10, "kategorie": "3"},
        {"text": "RYCHLOVKA: Kolik měsíců má jeden kalendářní rok?", "spravne": "12", "typ": "casovka", "limit": 10, "kategorie": "3"}
    ]

    print(f"{ZLUTA}=== VÍTEJ V PARÁDNÍM MULTI-KVÍZU ===\n{RESET}")
    jmeno_hrace = input("Zadej své jméno: ").strip()
    
    try:
        with open("rekord.txt", "r", encoding="utf-8") as soubor:
            osobni_rekord = int(soubor.read())
            print(f"{ZELENA}> Načten tvůj historický rekord ze souboru: {osobni_rekord} bodů!{RESET}")
    except FileNotFoundError:
        osobni_rekord = 0
        print(f"{ZLUTA}> Zatím nemáš uložený žádný rekord. Čas ho vytvořit!{RESET}")

    while True:
        print("\nVyber si téma kvízu:")
        print("1) Geografie")
        print("2) Věda a technika")
        print("3) Rychlovky")
        
        volba_kategorie = input("Zadej číslo kategorie (1/2/3): ").strip()
        if volba_kategorie not in ["1", "2", "3"]:
            print(f"{CERVENA}Neplatná volba! Zkus to znovu.{RESET}")
            continue
            
        aktivni_otazky = []
        for o in otazky:
            if o["kategorie"] == volba_kategorie:
                aktivni_otazky.append(o)

        random.shuffle(aktivni_otazky)
        skore = 0
        zivoty = 3
        
        for otazka in aktivni_otazky:
            print("-" * 30)
            print(f"Tvůj stav: {'❤️ ' * zivoty}")
            print(f"(Pro ukončení kvízu napiš slovo 'konec')")
            print(f"{ZLUTA}{otazka['text']}{RESET}")
            
            if otazka["typ"] == "casovka":
                print(f"{CERVENA}!!! POZOR, máš jen {otazka['limit']} sekund !!!{RESET}")
                start_cas = time.time()
                odpoved = input("Tvoje odpověď: ")
                konec_cas = time.time()
                uplynuly_cas = konec_cas - start_cas
                
                if odpoved.lower().strip() == "konec":
                    print(f"\n{ZLUTA}>>> HRA PŘEDČASNĚ UKONČENA HRÁČEM.{RESET}")
                    break

                if uplynuly_cas > otazka["limit"]:
                    print(f"{CERVENA}>>> Čas vypršel! Trvalo ti to {uplynuly_cas:.1f} s.{RESET}")
                    print(f"{CERVENA}>>> Správně bylo: {otazka['spravne']}{RESET}")
                    zivoty -= 1
                else:
                    kontrola_spravnosti = otazka["spravne"]
            
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
                
                odpoved = input("Tvoje volba (a/b/c nebo konec): ").lower().strip()
                if odpoved == "konec":
                    print(f"\n{ZLUTA}>>> HRA PŘEDČASNĚ UKONČENA HRÁČEM.{RESET}")
                    break
                kontrola_spravnosti = pismeno_spravne_odpovedi
                
            else:
                odpoved = input("Tvoje odpověď: ")
                if odpoved.lower().strip() == "konec":
                    print(f"\n{ZLUTA}>>> HRA PŘEDČASNĚ UKONČENA HRÁČEM.{RESET}")
                    break
                kontrola_spravnosti = otazka["spravne"]

            if otazka["typ"] != "casovka" or (otazka["typ"] == "casovka" and uplynuly_cas <= otazka["limit"]):
                # Vyhodnocení odpovědi s barevným odlišením (ZELENA pro úspěch, CERVENA pro fail)
                if odpoved.lower().strip() == kontrola_spravnosti.lower().strip():
                    print(f"{ZELENA}>>> Správně!{RESET}")
                    skore += 1
                else:
                    if otazka["typ"] == "volba":
                        print(f"{CERVENA}>>> Špatně! Správná volba byla: {kontrola_spravnosti}) {otazka['spravne']}{RESET}")
                    else:
                        print(f"{CERVENA}>>> Špatně! Správně bylo: {otazka['spravne']}{RESET}")
                    zivoty -= 1
            
            if zivoty <= 0:
                print(f"{CERVENA}\n" + "💀" * 15)
                print("   GAME OVER! DOŠLY TI ŽIVOTY.")
                print("💀" * 15 + f"{RESET}")
                break
        
        if skore > osobni_rekord:
            osobni_rekord = skore
            print(f"{ZELENA}\n*** NOVÝ HISTORICKÝ REKORD! ***{RESET}")
            
            with open("rekord.txt", "w", encoding="utf-8") as soubor:
                soubor.write(str(osobni_rekord))
                print(f"{ZELENA}> (Rekord byl bezpečně uložen na tvůj disk){RESET}")

        print("\n" + "=" * 35)
        print(f"Hráč: {jmeno_hrace}")
        print(f"Skóre z této hry: {skore}")
        print(f"Tvůj historický rekord: {osobni_rekord}")
        print("=" * 35)

        if input("Chceš hrát znovu? (ano/ne): ").lower().strip() != "ano":
            print(f"Díky za hru, {jmeno_hrace}! Měj se.")
            break

if __name__ == "__main__":
    spustit_kviz()
