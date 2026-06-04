# Kviz - SEDUMNÁCTÁ VERZE

import random
import time

def spustit_kviz():
    otazky = [
        # --- KATEGORIE 1: Geografie (Nyní 10 otázek) ---
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

        # --- KATEGORIE 2: Věda a technika (Zatím 5 otázek) ---
        {"text": "Kolik je 5 + 5?", "moznosti": ["10", "12", "8"], "spravne": "10", "typ": "volba", "kategorie": "2"},
        {"text": "Která planeta je nejblíže Slunci?", "moznosti": ["Venuše", "Merkur", "Země"], "spravne": "Merkur", "typ": "volba", "kategorie": "2"},
        {"text": "Jaký chemický prvek má značku O?", "moznosti": ["Zlato", "Kyslík", "Olovo"], "spravne": "Kyslík", "typ": "volba", "kategorie": "2"},
        {"text": "Který savec umí jako jediný aktivně létat?", "spravne": "netopýr", "typ": "otevrena", "kategorie": "2"},
        {"text": "Který programovací jazyk používáme pro tento kvíz?", "moznosti": ["Java", "Python", "C++"], "spravne": "Python", "typ": "volba", "kategorie": "2"},

        # --- KATEGORIE 3: Rychlovky (Zatím 5 otázek) ---
        {"text": "RYCHLOVKA: Kolik je 7 * 8?", "spravne": "56", "typ": "casovka", "limit": 10, "kategorie": "3"},
        {"text": "RYCHLOVKA: Jaká je chemická značka vody?", "spravne": "H2O", "typ": "casovka", "limit": 10, "kategorie": "3"},
        {"text": "RYCHLOVKA: Jaké je hlavní město Slovenska?", "spravne": "Bratislava", "typ": "casovka", "limit": 10, "kategorie": "3"},
        {"text": "RYCHLOVKA: Kolik minut má jedna hodina?", "spravne": "60", "typ": "casovka", "limit": 10, "kategorie": "3"},
        {"text": "RYCHLOVKA: Napiš zkratku České republiky:", "spravne": "ČR", "typ": "casovka", "limit": 10, "kategorie": "3"}
    ]

    print("=== VÍTEJ V PARÁDNÍM MULTI-KVÍZU ===")
    jmeno_hrace = input("Zadej své jméno: ").strip()
    
    try:
        with open("rekord.txt", "r", encoding="utf-8") as soubor:
            osobni_rekord = int(soubor.read())
            print(f"> Načten tvůj historický rekord ze souboru: {osobni_rekord} bodů!")
    except FileNotFoundError:
        osobni_rekord = 0
        print("> Zatím nemáš uložený žádný rekord. Čas ho vytvořit!")

    while True:
        print("\nVyber si téma kvízu:")
        print("1) Geografie")
        print("2) Věda a technika")
        print("3) Rychlovky")
        
        volba_kategorie = input("Zadej číslo kategorie (1/2/3): ").strip()
        if volba_kategorie not in ["1", "2", "3"]:
            print("Neplatná volba! Zkus to znovu.")
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
                
                odpoved = input("Tvoje volba (a/b/c): ").lower().strip()
                kontrola_spravnosti = pismeno_spravne_odpovedi
                
            else:
                odpoved = input("Tvoje odpověď: ")
                kontrola_spravnosti = otazka["spravne"]

            if otazka["typ"] != "casovka" or (otazka["typ"] == "casovka" and uplynuly_cas <= otazka["limit"]):
                if odpoved.lower().strip() == kontrola_spravnosti.lower().strip():
                    print(">>> Správně!")
                    skore += 1
                else:
                    if otazka["typ"] == "volba":
                        print(f">>> Špatně! Správná volba byla: {kontrola_spravnosti}) {otazka['spravne']}")
                    else:
                        print(f">>> Špatně! Správně bylo: {otazka['spravne']}")
                    zivoty -= 1
            
            if zivoty <= 0:
                print("\n" + "💀" * 15)
                print("   GAME OVER! DOŠLY TI ŽIVOTY.")
                print("💀" * 15)
                break
        
        if skore > osobni_rekord:
            osobni_rekord = skore
            print("\n*** NOVÝ HISTORICKÝ REKORD! ***")
            
            with open("rekord.txt", "w", encoding="utf-8") as soubor:
                soubor.write(str(osobni_rekord))
                print("> (Rekord byl bezpečně uložen na tvůj disk)")

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
